# Python Code Snippets

Collection of useful Python code snippets for web development, data processing, and automation.

## 🚀 FastAPI Examples

### REST API with CRUD Operations

```python
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import models, schemas, database

app = FastAPI(title="ITMC API Example")

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/items/", response_model=List[schemas.Item])
async def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all items with pagination"""
    items = db.query(models.Item).offset(skip).limit(limit).all()
    return items

@app.get("/items/{item_id}", response_model=schemas.Item)
async def read_item(item_id: int, db: Session = Depends(get_db)):
    """Get a specific item by ID"""
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items/", response_model=schemas.Item)
async def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    """Create a new item"""
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/items/{item_id}", response_model=schemas.Item)
async def update_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db)):
    """Update an existing item"""
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    for key, value in item.dict(exclude_unset=True).items():
        setattr(db_item, key, value)
    
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    """Delete an item"""
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted successfully"}
```

### Authentication with JWT

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional

SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against a hash"""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Generate password hash"""
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Create JWT access token"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """Get current authenticated user"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    # Get user from database here
    return {"username": username}

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """Login endpoint to get access token"""
    # Verify user credentials here
    user = {"username": form_data.username}  # Get from database
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(current_user: dict = Depends(get_current_user)):
    """Get current user profile"""
    return current_user
```

## 🗄️ Database Operations

### SQLAlchemy Models and Session Management

```python
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

DATABASE_URL = "postgresql://user:password@localhost/dbname"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Integer, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    orders = relationship("Order", back_populates="user")

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    total = Column(Float)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="orders")

# Create tables
Base.metadata.create_all(bind=engine)

# Context manager for database sessions
from contextlib import contextmanager

@contextmanager
def get_db_session():
    """Database session context manager"""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

# Usage example
def create_user(email: str, password: str):
    with get_db_session() as db:
        user = User(email=email, hashed_password=hash_password(password))
        db.add(user)
        return user
```

### Async Database Operations with AsyncIO

```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select

DATABASE_URL = "postgresql+asyncpg://user:password@localhost/dbname"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def get_users():
    """Get all users asynchronously"""
    async with async_session() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()
        return users

async def create_user_async(email: str, password: str):
    """Create user asynchronously"""
    async with async_session() as session:
        user = User(email=email, hashed_password=password)
        session.add(user)
        await session.commit()
        return user

async def get_user_by_email(email: str):
    """Get user by email asynchronously"""
    async with async_session() as session:
        result = await session.execute(
            select(User).where(User.email == email)
        )
        user = result.scalar_one_or_none()
        return user
```

## 📊 Data Processing

### Pandas Data Analysis

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def analyze_sales_data(csv_file: str) -> dict:
    """
    Analyze sales data and return key metrics
    
    Args:
        csv_file: Path to CSV file containing sales data
        
    Returns:
        Dictionary with analysis results
    """
    # Load data
    df = pd.read_csv(csv_file)
    df['date'] = pd.to_datetime(df['date'])
    
    # Calculate metrics
    total_sales = df['amount'].sum()
    avg_order_value = df['amount'].mean()
    total_orders = len(df)
    
    # Group by product
    product_sales = df.groupby('product')['amount'].agg(['sum', 'count', 'mean'])
    top_products = product_sales.sort_values('sum', ascending=False).head(10)
    
    # Time-based analysis
    df['month'] = df['date'].dt.to_period('M')
    monthly_sales = df.groupby('month')['amount'].sum()
    
    # Growth rate
    df['month_num'] = df['date'].dt.to_period('M')
    monthly_totals = df.groupby('month_num')['amount'].sum()
    growth_rate = monthly_totals.pct_change().mean() * 100
    
    return {
        'total_sales': float(total_sales),
        'avg_order_value': float(avg_order_value),
        'total_orders': int(total_orders),
        'top_products': top_products.to_dict(),
        'monthly_sales': monthly_sales.to_dict(),
        'growth_rate': float(growth_rate)
    }

# Example usage
results = analyze_sales_data('sales_data.csv')
print(f"Total Sales: ${results['total_sales']:,.2f}")
print(f"Average Order Value: ${results['avg_order_value']:.2f}")
print(f"Monthly Growth Rate: {results['growth_rate']:.2f}%")
```

## 🔒 Security Utilities

### Password Validation and Hashing

```python
import re
import secrets
import string
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def validate_password(password: str) -> tuple[bool, str]:
    """
    Validate password strength
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter"
    
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter"
    
    if not re.search(r"\d", password):
        return False, "Password must contain at least one digit"
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character"
    
    return True, "Password is valid"

def hash_password(password: str) -> str:
    """Hash a password using bcrypt"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hash"""
    return pwd_context.verify(plain_password, hashed_password)

def generate_secure_token(length: int = 32) -> str:
    """Generate a secure random token"""
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

# Example usage
password = "MySecureP@ssw0rd"
is_valid, message = validate_password(password)
if is_valid:
    hashed = hash_password(password)
    print(f"Password hash: {hashed}")
```

## 🚀 Async HTTP Clients

### HTTPX Async Client

```python
import httpx
import asyncio
from typing import List, Dict, Any

class APIClient:
    """Async HTTP client for API interactions"""
    
    def __init__(self, base_url: str, api_key: str = None):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}
        
    async def get(self, endpoint: str, params: Dict = None) -> Dict[str, Any]:
        """Make GET request"""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/{endpoint}",
                headers=self.headers,
                params=params
            )
            response.raise_for_status()
            return response.json()
    
    async def post(self, endpoint: str, data: Dict) -> Dict[str, Any]:
        """Make POST request"""
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/{endpoint}",
                headers=self.headers,
                json=data
            )
            response.raise_for_status()
            return response.json()
    
    async def fetch_multiple(self, endpoints: List[str]) -> List[Dict[str, Any]]:
        """Fetch multiple endpoints concurrently"""
        async with httpx.AsyncClient() as client:
            tasks = [
                client.get(f"{self.base_url}/{endpoint}", headers=self.headers)
                for endpoint in endpoints
            ]
            responses = await asyncio.gather(*tasks)
            return [r.json() for r in responses]

# Usage example
async def main():
    client = APIClient("https://api.example.com", api_key="your-api-key")
    
    # Single request
    user = await client.get("users/123")
    
    # Multiple concurrent requests
    endpoints = ["users/1", "users/2", "users/3"]
    users = await client.fetch_multiple(endpoints)
    
    return users

# Run
asyncio.run(main())
```

## 🔗 Related Resources

- [JavaScript Snippets](javascript.md)
- [DevOps Snippets](devops.md)
- [Development Services](../services/development.md)
