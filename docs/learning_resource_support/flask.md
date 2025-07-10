# Flask (REST API) Learning Resource

## Overview
Flask is a lightweight WSGI web application framework in Python, ideal for building REST APIs and simple web apps.

## Key Concepts & Glossary
- **Route**: URL pattern mapped to a Python function
- **Blueprint**: Modular app structure
- **Request/Response**: HTTP communication objects
- **Flask Extensions**: Add-ons for extra features (e.g., Flask-RESTful)

## Syntax & Examples
```python
from flask import Flask
app = Flask(__name__)
@app.route('/hello')
def hello():
    return 'Hello, World!'
if __name__ == '__main__':
    app.run()
```

## Common Use Cases
- RESTful APIs
- Microservices
- Prototyping web apps

## Setup & Usage
```bash
pip install flask
python app.py
```

## Best Practices
- Use Blueprints for modularity
- Validate input data
- Use environment variables for config

## External Learning Links
- [Flask Docs](https://flask.palletsprojects.com/)
- [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [Awesome Flask](https://github.com/humiaozuzu/awesome-flask)

## How Flask is Used in This Project
- Provides a traditional REST API for data and analysis
- Health check and data endpoints
- Entry point: `src/api/rest_api.py` 

## Core Concepts Used in This Project
- Used for traditional REST API endpoints.
- Chosen for simplicity, maturity, and wide adoption.
- Used routes, blueprints, and request/response objects.

## Ignored/Alternative Concepts
- Not used: Django REST Framework, FastAPI (for REST), Falcon, Bottle.
- Reason: Flask is lightweight, easy to set up, and familiar to most Python devs.

## Other Concepts You Could Use
- Flask-RESTful for more structured APIs
- Flask-SQLAlchemy for ORM/database
- Flask-JWT for authentication

## Technology Foundations
- Built on Werkzeug WSGI toolkit and Jinja2 templating.

## Advantages & Disadvantages
**Advantages:**
- Simple and flexible
- Huge ecosystem and community
- Easy to learn and extend

**Disadvantages:**
- Synchronous only (no async)
- Manual validation and docs
- Less performant for high concurrency 

## Project Keywords Used (with Use & Summary)
- **Flask**: Main app object; creates the REST API server.
- **@app.route**: Decorator for defining API endpoints (e.g., /api/health).
- **request**: Accesses incoming request data (e.g., POST payloads).
- **jsonify**: Converts Python objects to JSON responses.
- **Blueprint**: Organizes API routes into modular sections (if used).
- **app.run**: Starts the Flask development server (used in local dev).
- **REST API endpoints**: Exposes data and analysis functions via HTTP.
- **Health check endpoint**: Simple GET endpoint to verify service status. 