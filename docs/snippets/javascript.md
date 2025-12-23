# JavaScript & TypeScript Code Snippets

Collection of modern JavaScript and TypeScript code examples for frontend and backend development.

## ⚛️ React Examples

### Custom Hooks

```typescript
import { useState, useEffect, useCallback, useRef } from 'react';

// useDebounce Hook
export function useDebounce<T>(value: T, delay: number): T {
    const [debouncedValue, setDebouncedValue] = useState<T>(value);

    useEffect(() => {
        const handler = setTimeout(() => {
            setDebouncedValue(value);
        }, delay);

        return () => {
            clearTimeout(handler);
        };
    }, [value, delay]);

    return debouncedValue;
}

// useLocalStorage Hook
export function useLocalStorage<T>(key: string, initialValue: T) {
    const [storedValue, setStoredValue] = useState<T>(() => {
        try {
            const item = window.localStorage.getItem(key);
            return item ? JSON.parse(item) : initialValue;
        } catch (error) {
            console.log(error);
            return initialValue;
        }
    });

    const setValue = (value: T | ((val: T) => T)) => {
        try {
            const valueToStore = value instanceof Function ? value(storedValue) : value;
            setStoredValue(valueToStore);
            window.localStorage.setItem(key, JSON.stringify(valueToStore));
        } catch (error) {
            console.log(error);
        }
    };

    return [storedValue, setValue] as const;
}

// useFetch Hook
export function useFetch<T>(url: string) {
    const [data, setData] = useState<T | null>(null);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<Error | null>(null);

    useEffect(() => {
        const abortController = new AbortController();

        fetch(url, { signal: abortController.signal })
            .then(response => {
                if (!response.ok) throw new Error('Network response was not ok');
                return response.json();
            })
            .then(data => {
                setData(data);
                setLoading(false);
            })
            .catch(error => {
                if (error.name !== 'AbortError') {
                    setError(error);
                    setLoading(false);
                }
            });

        return () => abortController.abort();
    }, [url]);

    return { data, loading, error };
}

// useIntersectionObserver Hook
export function useIntersectionObserver(
    elementRef: React.RefObject<Element>,
    { threshold = 0, root = null, rootMargin = '0%' }: IntersectionObserverInit
): IntersectionObserverEntry | undefined {
    const [entry, setEntry] = useState<IntersectionObserverEntry>();

    useEffect(() => {
        const node = elementRef?.current;
        const hasIOSupport = !!window.IntersectionObserver;

        if (!hasIOSupport || !node) return;

        const observer = new IntersectionObserver(
            ([entry]) => setEntry(entry),
            { threshold, root, rootMargin }
        );

        observer.observe(node);

        return () => observer.disconnect();
    }, [elementRef, threshold, root, rootMargin]);

    return entry;
}
```

### React Context with TypeScript

```typescript
import React, { createContext, useContext, useReducer, ReactNode } from 'react';

// Types
interface User {
    id: string;
    name: string;
    email: string;
}

interface AuthState {
    user: User | null;
    isAuthenticated: boolean;
    loading: boolean;
}

type AuthAction =
    | { type: 'LOGIN_SUCCESS'; payload: User }
    | { type: 'LOGOUT' }
    | { type: 'SET_LOADING'; payload: boolean };

interface AuthContextType extends AuthState {
    login: (email: string, password: string) => Promise<void>;
    logout: () => void;
}

// Initial state
const initialState: AuthState = {
    user: null,
    isAuthenticated: false,
    loading: true,
};

// Reducer
function authReducer(state: AuthState, action: AuthAction): AuthState {
    switch (action.type) {
        case 'LOGIN_SUCCESS':
            return {
                ...state,
                user: action.payload,
                isAuthenticated: true,
                loading: false,
            };
        case 'LOGOUT':
            return {
                ...state,
                user: null,
                isAuthenticated: false,
                loading: false,
            };
        case 'SET_LOADING':
            return {
                ...state,
                loading: action.payload,
            };
        default:
            return state;
    }
}

// Context
const AuthContext = createContext<AuthContextType | undefined>(undefined);

// Provider
export function AuthProvider({ children }: { children: ReactNode }) {
    const [state, dispatch] = useReducer(authReducer, initialState);

    const login = async (email: string, password: string) => {
        dispatch({ type: 'SET_LOADING', payload: true });
        try {
            const response = await fetch('/api/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, password }),
            });
            const user = await response.json();
            dispatch({ type: 'LOGIN_SUCCESS', payload: user });
        } catch (error) {
            dispatch({ type: 'SET_LOADING', payload: false });
            throw error;
        }
    };

    const logout = () => {
        localStorage.removeItem('token');
        dispatch({ type: 'LOGOUT' });
    };

    return (
        <AuthContext.Provider value={{ ...state, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
}

// Hook
export function useAuth() {
    const context = useContext(AuthContext);
    if (context === undefined) {
        throw new Error('useAuth must be used within an AuthProvider');
    }
    return context;
}
```

### React Component Patterns

```typescript
import React, { useState, memo, useCallback } from 'react';

// Compound Component Pattern
interface TabsContextType {
    activeTab: string;
    setActiveTab: (tab: string) => void;
}

const TabsContext = React.createContext<TabsContextType | undefined>(undefined);

export function Tabs({ children, defaultTab }: { children: React.ReactNode; defaultTab: string }) {
    const [activeTab, setActiveTab] = useState(defaultTab);

    return (
        <TabsContext.Provider value={{ activeTab, setActiveTab }}>
            <div className="tabs">{children}</div>
        </TabsContext.Provider>
    );
}

Tabs.List = function TabsList({ children }: { children: React.ReactNode }) {
    return <div className="tabs-list">{children}</div>;
};

Tabs.Tab = function Tab({ id, children }: { id: string; children: React.ReactNode }) {
    const context = React.useContext(TabsContext);
    if (!context) throw new Error('Tab must be used within Tabs');

    const { activeTab, setActiveTab } = context;
    const isActive = activeTab === id;

    return (
        <button
            className={`tab ${isActive ? 'active' : ''}`}
            onClick={() => setActiveTab(id)}
        >
            {children}
        </button>
    );
};

Tabs.Panel = function TabPanel({ id, children }: { id: string; children: React.ReactNode }) {
    const context = React.useContext(TabsContext);
    if (!context) throw new Error('TabPanel must be used within Tabs');

    const { activeTab } = context;
    if (activeTab !== id) return null;

    return <div className="tab-panel">{children}</div>;
};

// Usage:
// <Tabs defaultTab="home">
//   <Tabs.List>
//     <Tabs.Tab id="home">Home</Tabs.Tab>
//     <Tabs.Tab id="profile">Profile</Tabs.Tab>
//   </Tabs.List>
//   <Tabs.Panel id="home">Home Content</Tabs.Panel>
//   <Tabs.Panel id="profile">Profile Content</Tabs.Panel>
// </Tabs>

// Render Props Pattern
interface MousePosition {
    x: number;
    y: number;
}

interface MouseTrackerProps {
    render: (position: MousePosition) => React.ReactNode;
}

export const MouseTracker: React.FC<MouseTrackerProps> = ({ render }) => {
    const [position, setPosition] = useState<MousePosition>({ x: 0, y: 0 });

    const handleMouseMove = useCallback((event: React.MouseEvent) => {
        setPosition({ x: event.clientX, y: event.clientY });
    }, []);

    return <div onMouseMove={handleMouseMove}>{render(position)}</div>;
};

// Usage:
// <MouseTracker render={({ x, y }) => (
//   <div>Mouse position: {x}, {y}</div>
// )} />
```

## 🚀 Node.js & Express

### Express REST API with TypeScript

```typescript
import express, { Request, Response, NextFunction } from 'express';
import { body, validationResult } from 'express-validator';
import jwt from 'jsonwebtoken';

const app = express();
app.use(express.json());

// Types
interface User {
    id: string;
    email: string;
    name: string;
}

interface AuthRequest extends Request {
    user?: User;
}

// Middleware
const authMiddleware = (req: AuthRequest, res: Response, next: NextFunction) => {
    const token = req.header('Authorization')?.replace('Bearer ', '');

    if (!token) {
        return res.status(401).json({ error: 'No token provided' });
    }

    try {
        const decoded = jwt.verify(token, process.env.JWT_SECRET!) as User;
        req.user = decoded;
        next();
    } catch (error) {
        res.status(401).json({ error: 'Invalid token' });
    }
};

const errorHandler = (err: Error, req: Request, res: Response, next: NextFunction) => {
    console.error(err.stack);
    res.status(500).json({
        error: 'Internal server error',
        message: process.env.NODE_ENV === 'development' ? err.message : undefined,
    });
};

// Validation middleware
const validateRequest = (req: Request, res: Response, next: NextFunction) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array() });
    }
    next();
};

// Routes
app.post(
    '/api/users',
    [
        body('email').isEmail().normalizeEmail(),
        body('password').isLength({ min: 8 }),
        body('name').trim().notEmpty(),
    ],
    validateRequest,
    async (req: Request, res: Response) => {
        try {
            const { email, password, name } = req.body;
            // Create user logic here
            const user = { id: '123', email, name };
            res.status(201).json({ user });
        } catch (error) {
            next(error);
        }
    }
);

app.get('/api/users/:id', authMiddleware, async (req: AuthRequest, res: Response) => {
    try {
        const { id } = req.params;
        // Get user logic here
        const user = { id, email: 'user@example.com', name: 'John Doe' };
        res.json({ user });
    } catch (error) {
        next(error);
    }
});

app.use(errorHandler);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```

### API Client Class

```typescript
class APIClient {
    private baseURL: string;
    private headers: Record<string, string>;

    constructor(baseURL: string, token?: string) {
        this.baseURL = baseURL;
        this.headers = {
            'Content-Type': 'application/json',
            ...(token && { Authorization: `Bearer ${token}` }),
        };
    }

    private async request<T>(
        endpoint: string,
        options: RequestInit = {}
    ): Promise<T> {
        const url = `${this.baseURL}${endpoint}`;
        const config: RequestInit = {
            ...options,
            headers: {
                ...this.headers,
                ...options.headers,
            },
        };

        try {
            const response = await fetch(url, config);

            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.message || 'API request failed');
            }

            return await response.json();
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    }

    async get<T>(endpoint: string): Promise<T> {
        return this.request<T>(endpoint, { method: 'GET' });
    }

    async post<T>(endpoint: string, data: any): Promise<T> {
        return this.request<T>(endpoint, {
            method: 'POST',
            body: JSON.stringify(data),
        });
    }

    async put<T>(endpoint: string, data: any): Promise<T> {
        return this.request<T>(endpoint, {
            method: 'PUT',
            body: JSON.stringify(data),
        });
    }

    async delete<T>(endpoint: string): Promise<T> {
        return this.request<T>(endpoint, { method: 'DELETE' });
    }

    setToken(token: string) {
        this.headers.Authorization = `Bearer ${token}`;
    }

    removeToken() {
        delete this.headers.Authorization;
    }
}

// Usage
const api = new APIClient('https://api.example.com');
const users = await api.get<User[]>('/users');
const newUser = await api.post<User>('/users', { name: 'John', email: 'john@example.com' });
```

## 🔧 Utility Functions

### Common JavaScript Utilities

```typescript
// Debounce function
export function debounce<T extends (...args: any[]) => any>(
    func: T,
    wait: number
): (...args: Parameters<T>) => void {
    let timeout: NodeJS.Timeout;
    return function executedFunction(...args: Parameters<T>) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Throttle function
export function throttle<T extends (...args: any[]) => any>(
    func: T,
    limit: number
): (...args: Parameters<T>) => void {
    let inThrottle: boolean;
    return function executedFunction(...args: Parameters<T>) {
        if (!inThrottle) {
            func(...args);
            inThrottle = true;
            setTimeout(() => (inThrottle = false), limit);
        }
    };
}

// Deep clone
export function deepClone<T>(obj: T): T {
    if (obj === null || typeof obj !== 'object') return obj;
    if (obj instanceof Date) return new Date(obj.getTime()) as any;
    if (obj instanceof Array) return obj.map(item => deepClone(item)) as any;
    if (obj instanceof Object) {
        const clonedObj = {} as T;
        for (const key in obj) {
            if (obj.hasOwnProperty(key)) {
                clonedObj[key] = deepClone(obj[key]);
            }
        }
        return clonedObj;
    }
    return obj;
}

// Format currency
export function formatCurrency(amount: number, currency: string = 'USD'): string {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency,
    }).format(amount);
}

// Format date
export function formatDate(date: Date | string, format: string = 'short'): string {
    const d = typeof date === 'string' ? new Date(date) : date;
    return new Intl.DateTimeFormat('en-US', {
        dateStyle: format as any,
    }).format(d);
}

// Generate random ID
export function generateId(length: number = 8): string {
    return Math.random()
        .toString(36)
        .substring(2, length + 2);
}

// Group array by key
export function groupBy<T>(array: T[], key: keyof T): Record<string, T[]> {
    return array.reduce((result, item) => {
        const groupKey = String(item[key]);
        if (!result[groupKey]) {
            result[groupKey] = [];
        }
        result[groupKey].push(item);
        return result;
    }, {} as Record<string, T[]>);
}

// Chunk array
export function chunk<T>(array: T[], size: number): T[][] {
    const chunks: T[][] = [];
    for (let i = 0; i < array.length; i += size) {
        chunks.push(array.slice(i, i + size));
    }
    return chunks;
}

// Sleep/delay
export function sleep(ms: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Retry with exponential backoff
export async function retry<T>(
    fn: () => Promise<T>,
    maxAttempts: number = 3,
    delay: number = 1000
): Promise<T> {
    for (let attempt = 1; attempt <= maxAttempts; attempt++) {
        try {
            return await fn();
        } catch (error) {
            if (attempt === maxAttempts) throw error;
            await sleep(delay * Math.pow(2, attempt - 1));
        }
    }
    throw new Error('Max attempts reached');
}
```

## 📊 Data Transformation

### Array and Object Utilities

```typescript
// Pick specific properties from object
export function pick<T, K extends keyof T>(obj: T, keys: K[]): Pick<T, K> {
    return keys.reduce((result, key) => {
        if (key in obj) {
            result[key] = obj[key];
        }
        return result;
    }, {} as Pick<T, K>);
}

// Omit specific properties from object
export function omit<T, K extends keyof T>(obj: T, keys: K[]): Omit<T, K> {
    const result = { ...obj };
    keys.forEach(key => delete result[key]);
    return result;
}

// Flatten nested array
export function flatten<T>(array: any[]): T[] {
    return array.reduce(
        (acc, val) => acc.concat(Array.isArray(val) ? flatten(val) : val),
        []
    );
}

// Remove duplicates from array
export function unique<T>(array: T[]): T[] {
    return Array.from(new Set(array));
}

// Sort array of objects by key
export function sortBy<T>(array: T[], key: keyof T, order: 'asc' | 'desc' = 'asc'): T[] {
    return [...array].sort((a, b) => {
        const aVal = a[key];
        const bVal = b[key];
        if (aVal < bVal) return order === 'asc' ? -1 : 1;
        if (aVal > bVal) return order === 'asc' ? 1 : -1;
        return 0;
    });
}

// Merge objects deeply
export function mergeDeep<T extends object>(target: T, ...sources: Partial<T>[]): T {
    if (!sources.length) return target;
    const source = sources.shift();

    if (isObject(target) && isObject(source)) {
        for (const key in source) {
            if (isObject(source[key])) {
                if (!target[key]) Object.assign(target, { [key]: {} });
                mergeDeep(target[key] as any, source[key] as any);
            } else {
                Object.assign(target, { [key]: source[key] });
            }
        }
    }

    return mergeDeep(target, ...sources);
}

function isObject(item: any): boolean {
    return item && typeof item === 'object' && !Array.isArray(item);
}
```

## 🔗 Related Resources

- [Python Snippets](python.md)
- [DevOps Snippets](devops.md)
- [Development Services](../services/development.md)
