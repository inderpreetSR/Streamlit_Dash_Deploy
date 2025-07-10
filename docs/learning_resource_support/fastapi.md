# FastAPI Learning Resource

## Overview
FastAPI is a modern, high-performance web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Key Concepts & Glossary
- **Path Operation**: API endpoint (route)
- **Pydantic**: Data validation and settings management
- **Dependency Injection**: Reusable components for routes
- **OpenAPI**: Auto-generated API docs

## Syntax & Examples
```python
from fastapi import FastAPI
app = FastAPI()
@app.get("/hello")
def read_root():
    return {"message": "Hello World"}
```

## Common Use Cases
- RESTful APIs
- Async microservices
- Auto-documented APIs

## Setup & Usage
```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

## Best Practices
- Use Pydantic models for request/response validation
- Leverage dependency injection for shared logic
- Use async endpoints for I/O-bound operations

## External Learning Links
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [FastAPI Crash Course (YouTube)](https://www.youtube.com/watch?v=0sOvCWFmrtA)
- [Awesome FastAPI](https://github.com/mjhea0/awesome-fastapi)

## How FastAPI is Used in This Project
- Provides modern, async API endpoints
- Auto-generated docs at `/docs` and `/redoc`
- Entry point: `src/api/fast_api.py` 

## Core Concepts Used in This Project
- Used for modern, async API endpoints.
- Chosen for speed, type safety, and auto-generated docs.
- Used Pydantic models, dependency injection, and async endpoints.

## Ignored/Alternative Concepts
- Not used: Django REST Framework, Flask-RESTful, Tornado, or Falcon.
- Reason: FastAPI is faster, more modern, and has better async support.

## Other Concepts You Could Use
- WebSockets for real-time APIs
- OAuth2/JWT authentication
- Background tasks and event hooks

## Technology Foundations
- Built on Starlette (ASGI) and Pydantic.

## Advantages & Disadvantages
**Advantages:**
- Extremely fast and async-ready
- Type-checked, auto-documented
- Modern Pythonic syntax

**Disadvantages:**
- Newer, smaller ecosystem than Flask/Django
- Some advanced features require Starlette knowledge 

## Project Keywords Used (with Use & Summary)
- **FastAPI**: Main app object; creates the API server.
- **@app.get**: Decorator for GET endpoints (e.g., health check, data info).
- **@app.post**: Decorator for POST endpoints (e.g., data filtering/export).
- **Pydantic**: Used for data validation and serialization of request/response models.
- **BaseModel**: Base class for defining Pydantic models.
- **Dependency injection**: Shares logic (e.g., DB/session) across endpoints.
- **async def**: Defines asynchronous endpoints for better performance.
- **uvicorn**: ASGI server to run FastAPI apps.
- **/docs (Swagger UI)**: Auto-generated interactive API documentation.
- **/redoc**: Alternative auto-generated API documentation.
- **Health check endpoint**: Simple GET endpoint to verify service status. 