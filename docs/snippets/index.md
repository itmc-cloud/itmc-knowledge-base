# Code Snippets

Welcome to the ITMC Cloud code snippets collection! Here you'll find reusable code examples, utilities, and best practices for various programming languages and technologies.

## 📚 Available Categories

<div class="grid cards" markdown>

-   :fontawesome-brands-python:{ .lg .middle } __Python Snippets__

    ---

    Python code examples including web frameworks, data processing, and automation

    [:octicons-arrow-right-24: Browse Python](python.md)

-   :fontawesome-brands-js:{ .lg .middle } __JavaScript/TypeScript__

    ---

    Modern JavaScript and TypeScript examples for frontend and backend development

    [:octicons-arrow-right-24: Browse JavaScript](javascript.md)

-   :material-cloud-cog:{ .lg .middle } __DevOps & Infrastructure__

    ---

    Docker, Kubernetes, Terraform, and CI/CD pipeline configurations

    [:octicons-arrow-right-24: Browse DevOps](devops.md)

</div>

## 🎯 How to Use These Snippets

All code snippets in this collection are:

- ✅ **Production-ready**: Tested and verified
- 📝 **Well-documented**: Includes explanations and comments
- 🔧 **Customizable**: Easy to adapt to your needs
- 🚀 **Best practices**: Follows industry standards

## 📋 Quick Index

### By Category

=== "Web Development"
    - [REST API Examples](python.md#rest-api)
    - [Authentication](javascript.md#authentication)
    - [Database Queries](python.md#database-operations)
    - [Frontend Components](javascript.md#react-components)

=== "DevOps"
    - [Docker Configurations](devops.md#docker)
    - [Kubernetes Manifests](devops.md#kubernetes)
    - [CI/CD Pipelines](devops.md#ci-cd)
    - [Infrastructure as Code](devops.md#terraform)

=== "Data & APIs"
    - [Data Processing](python.md#data-processing)
    - [API Integration](javascript.md#api-clients)
    - [Caching Strategies](python.md#caching)
    - [Database Migrations](python.md#migrations)

## 🔍 Most Popular Snippets

### 1. Docker Multi-Stage Build
```dockerfile
# Optimized Docker build for Node.js applications
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
```

### 2. FastAPI REST Endpoint
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
async def create_item(item: Item):
    return {"item": item, "status": "created"}
```

### 3. React Custom Hook
```typescript
import { useState, useEffect } from 'react';

function useApi<T>(url: string) {
    const [data, setData] = useState<T | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<Error | null>(null);

    useEffect(() => {
        fetch(url)
            .then(res => res.json())
            .then(setData)
            .catch(setError)
            .finally(() => setLoading(false));
    }, [url]);

    return { data, loading, error };
}
```

## 🏷️ Tags

Browse snippets by tags:

- `#api` - API development and integration
- `#database` - Database operations and queries
- `#auth` - Authentication and authorization
- `#deployment` - Deployment and infrastructure
- `#testing` - Testing frameworks and examples
- `#security` - Security best practices
- `#performance` - Performance optimization

## 🤝 Contributing Snippets

Want to add your own snippets? We welcome contributions!

1. Fork the repository
2. Add your snippet to the appropriate category
3. Include:
   - Clear description
   - Code example
   - Use case explanation
   - Dependencies (if any)
4. Submit a pull request

### Snippet Template

```markdown
### Snippet Title

**Description**: Brief explanation of what this code does

**Use Case**: When and why to use this snippet

**Dependencies**:
- Package 1
- Package 2

**Code**:
\`\`\`language
// Your code here
\`\`\`

**Example Usage**:
\`\`\`language
// Example of how to use the snippet
\`\`\`
```

## 📊 Snippet Statistics

- **Total Snippets**: 50+
- **Languages Covered**: 5+
- **Categories**: 10+
- **Last Updated**: December 2025

## 🔗 Related Resources

- [Getting Started Guide](../guides/getting-started.md)
- [Development Services](../services/development.md)
- [GitHub Repository](https://github.com/itmc-cloud/itmc-knowledge-base)

---

Can't find what you're looking for? [Request a snippet](https://github.com/itmc-cloud/itmc-knowledge-base/issues/new) or [contribute your own](../guides/getting-started.md#contributing)!
