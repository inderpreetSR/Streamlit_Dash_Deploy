# 🚀 Deployment Guide - Streamlit & Dash Insights Project

## 📋 Table of Contents

1. [Overview](#overview)
2. [API Comparison](#api-comparison)
3. [Deployment Options](#deployment-options)
4. [Docker Deployment](#docker-deployment)
5. [Local Development](#local-development)
6. [Production Deployment](#production-deployment)
7. [API Documentation](#api-documentation)
8. [Troubleshooting](#troubleshooting)

## 🎯 Overview

This project now includes **complete deployment capabilities** with both **REST API** and **FastAPI** options. The deployment system provides:

- **Containerized Services**: Docker-based deployment
- **Dual API Support**: Traditional REST API and modern FastAPI
- **Load Balancing**: Nginx reverse proxy
- **Health Monitoring**: Built-in health checks
- **Easy Management**: One-command deployment scripts

## 🔄 API Comparison

### **REST API (Flask) vs FastAPI**

| Feature | REST API (Flask) | FastAPI |
|---------|------------------|---------|
| **Framework** | Flask (Traditional) | FastAPI (Modern) |
| **Performance** | Good | Excellent (Async) |
| **Documentation** | Manual | Auto-generated |
| **Type Validation** | Manual | Automatic (Pydantic) |
| **Learning Curve** | Easy | Moderate |
| **Use Case** | Simple APIs | Complex, high-performance APIs |

### **Why Both APIs?**

1. **REST API (Flask)**:
   - **Simple and Familiar**: Easy to understand and modify
   - **Traditional**: Works with existing REST clients
   - **Lightweight**: Minimal overhead
   - **Good for**: Simple data access, legacy integration

2. **FastAPI**:
   - **High Performance**: Async support, faster response times
   - **Auto Documentation**: Interactive API docs at `/docs`
   - **Type Safety**: Automatic validation with Pydantic
   - **Modern Features**: WebSocket support, background tasks
   - **Good for**: Complex APIs, microservices, high-traffic applications

## 🚀 Deployment Options

### **Option 1: Docker Compose (Recommended)**
```bash
# One-command deployment
./deploy.sh          # Linux/Mac
deploy.bat           # Windows
```

### **Option 2: Individual Services**
```bash
# Start services individually
docker-compose up streamlit
docker-compose up dash
docker-compose up rest-api
docker-compose up fastapi
```

### **Option 3: Local Development**
```bash
# Run without Docker
python src/streamlit/app.py
python src/dash/app.py
python src/api/rest_api.py
python src/api/fast_api.py
```

## 🐳 Docker Deployment

### **Prerequisites**
- Docker Desktop installed
- Docker Compose installed
- Data file in `Data/raw/test.csv`

### **Quick Start**
```bash
# 1. Clone the repository
git clone <repository>
cd Streamlit_Dash_Deploy

# 2. Add your data file
cp your_data.csv Data/raw/test.csv

# 3. Deploy everything
./deploy.sh
```

### **Service Architecture**
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Nginx Proxy   │    │   Streamlit     │    │   Dash App      │
│   Port: 80      │    │   Port: 8501    │    │   Port: 8050    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────────┐    ┌─────────────────┐
                    │   REST API      │    │   FastAPI       │
                    │   Port: 5000    │    │   Port: 8000    │
                    └─────────────────┘    └─────────────────┘
```

### **Available Services**
| Service | URL | Description |
|---------|-----|-------------|
| **Streamlit** | http://localhost:8501 | Main dashboard |
| **Dash** | http://localhost:8050 | Advanced dashboard |
| **REST API** | http://localhost:5000 | Traditional API |
| **FastAPI** | http://localhost:8000 | Modern API |
| **FastAPI Docs** | http://localhost:8000/docs | Interactive documentation |
| **FastAPI ReDoc** | http://localhost:8000/redoc | Alternative documentation |

## 🗺️ Deployment Architecture

The following diagram illustrates the deployment flow and how each service interacts in the production environment:

```mermaid
flowchart TD
    User["User"] --> Browser["Web Browser"]
    Browser --> Nginx["Nginx Reverse Proxy"]
    Nginx -- "/" --> Streamlit["Streamlit Service"]
    Nginx -- "/dash" --> Dash["Dash Service"]
    Nginx -- "/api" --> RESTAPI["REST API (Flask)"]
    Nginx -- "/fastapi" --> FastAPI["FastAPI"]
    Streamlit --- Data["Data Volume"]
    Dash --- Data
    RESTAPI --- Data
    FastAPI --- Data
    Streamlit --- Logs["Logs Volume"]
    Dash --- Logs
    RESTAPI --- Logs
    FastAPI --- Logs
    Streamlit -- health --> Nginx
    Dash -- health --> Nginx
    RESTAPI -- health --> Nginx
    FastAPI -- health --> Nginx
    style Nginx fill:#e1f5fe
    style Streamlit fill:#e8f5e8
    style Dash fill:#e8f5e8
    style RESTAPI fill:#fff3e0
    style FastAPI fill:#fff3e0
    style Data fill:#f3e5f5
    style Logs fill:#f3e5f5
```

**Deployment Flow:**
- Users access the system via a web browser, connecting to the Nginx reverse proxy.
- Nginx routes requests to the appropriate service based on the URL path:
  - `/` → Streamlit dashboard
  - `/dash` → Dash dashboard
  - `/api` → REST API (Flask)
  - `/fastapi` → FastAPI endpoints
- All services share access to the data and logs volumes for persistent storage and logging.
- Health checks are routed through Nginx to monitor service status.

## 💻 Local Development

### **Setup Environment**
```bash
# 1. Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start services
```

### **Start Individual Services**
```bash
# Streamlit
cd src/streamlit
streamlit run app.py

# Dash
cd src/dash
python app.py

# REST API
cd src/api
python rest_api.py

# FastAPI
cd src/api
python fast_api.py
```

## 🏭 Production Deployment

### **Docker Production Setup**
```bash
# 1. Build production images
docker-compose -f docker-compose.prod.yml build

# 2. Start with production settings
docker-compose -f docker-compose.prod.yml up -d

# 3. Monitor services
docker-compose logs -f
```

### **Environment Variables**
```bash
# Production settings
export FLASK_ENV=production
export DEBUG_MODE=false
export SECRET_KEY=your-secret-key
export DATABASE_URL=postgresql://user:pass@host:port/db
```

### **SSL/HTTPS Setup**
```bash
# 1. Generate SSL certificates
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout ssl/nginx.key -out ssl/nginx.crt

# 2. Update nginx.conf with SSL
# 3. Restart nginx container
docker-compose restart nginx
```

## 📚 API Documentation

### **REST API Endpoints**

#### **Health Check**
```bash
GET /api/health
```
```json
{
  "status": "healthy",
  "timestamp": "2025-01-10T10:30:00",
  "data_available": true
}
```

#### **Data Information**
```bash
GET /api/data/info
```
```json
{
  "success": true,
  "data": {
    "total_rows": 1000,
    "total_columns": 310,
    "memory_usage_mb": 45.2
  }
}
```

#### **Data Sample**
```bash
GET /api/data/sample?size=100
```
```json
{
  "success": true,
  "data": [...],
  "sample_size": 100
}
```

#### **Analysis Endpoints**
```bash
GET /api/analysis/gender
GET /api/analysis/income
GET /api/analysis/loan
```

#### **Data Filtering**
```bash
POST /api/data/filter
Content-Type: application/json

{
  "column": "gender",
  "value": "Male",
  "operator": "equals"
}
```

### **FastAPI Endpoints**

#### **Interactive Documentation**
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

#### **Health Check**
```bash
GET /health
```
```json
{
  "status": "healthy",
  "timestamp": "2025-01-10T10:30:00",
  "data_available": true,
  "version": "1.0.0"
}
```

#### **Data Endpoints**
```bash
GET /data/info
GET /data/sample?size=100
GET /data/columns
POST /data/filter
```

#### **Analysis Endpoints**
```bash
GET /analysis/gender
GET /analysis/income
GET /analysis/loan
GET /analysis/correlation
```

#### **Performance Statistics**
```bash
GET /stats/performance
```

## 🔧 Management Commands

### **Docker Commands**
```bash
# View all services
docker-compose ps

# View logs
docker-compose logs -f
docker-compose logs streamlit
docker-compose logs rest-api

# Restart services
docker-compose restart
docker-compose restart fastapi

# Stop all services
docker-compose down

# Update and restart
docker-compose pull
docker-compose up -d
```

### **Health Checks**
```bash
# Check all services
curl http://localhost:8501  # Streamlit
curl http://localhost:8050  # Dash
curl http://localhost:5000  # REST API
curl http://localhost:8000  # FastAPI

# API health endpoints
curl http://localhost:5000/api/health
curl http://localhost:8000/health
```

## 🐛 Troubleshooting

### **Common Issues**

#### **1. Port Conflicts**
```bash
# Check what's using the ports
netstat -tulpn | grep :8501
netstat -tulpn | grep :5000
netstat -tulpn | grep :8000

# Change ports in docker-compose.yml
ports:
  - "8502:8501"  # Use different host port
```

#### **2. Data File Issues**
```bash
# Check if data file exists
ls -la Data/raw/test.csv

# Check file permissions
chmod 644 Data/raw/test.csv

# Verify file format
head -5 Data/raw/test.csv
```

#### **3. Memory Issues**
```bash
# Check Docker memory usage
docker stats

# Increase Docker memory limit
# Docker Desktop > Settings > Resources > Memory: 4GB+
```

#### **4. Service Not Starting**
```bash
# Check service logs
docker-compose logs streamlit
docker-compose logs rest-api
docker-compose logs fastapi

# Check service status
docker-compose ps

# Restart specific service
docker-compose restart streamlit
```

### **Performance Optimization**

#### **1. Increase Resources**
```yaml
# docker-compose.yml
services:
  streamlit:
    deploy:
      resources:
        limits:
          memory: 2G
          cpus: '1.0'
```

#### **2. Enable Caching**
```python
# In FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost", encoding="utf8")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
```

#### **3. Database Optimization**
```python
# Use connection pooling
DATABASE_URL = "postgresql://user:pass@host:port/db?pool_size=20&max_overflow=30"
```

## 📊 Monitoring and Logging

### **Log Management**
```bash
# View real-time logs
docker-compose logs -f --tail=100

# Save logs to file
docker-compose logs > deployment.log

# Monitor specific service
docker-compose logs -f streamlit
```

### **Health Monitoring**
```bash
# Create health check script
#!/bin/bash
services=(
    "http://localhost:8501"
    "http://localhost:8050"
    "http://localhost:5000"
    "http://localhost:8000"
)

for service in "${services[@]}"; do
    if curl -s "$service" > /dev/null; then
        echo "✅ $service is healthy"
    else
        echo "❌ $service is down"
    fi
done
```

### **Performance Metrics**
```bash
# Monitor resource usage
docker stats --format "table {{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}"

# Check API response times
curl -w "@curl-format.txt" -o /dev/null -s "http://localhost:8000/health"
```

## 🎉 Success Metrics

### **Deployment Checklist**
- ✅ All services start successfully
- ✅ Health checks pass
- ✅ APIs respond correctly
- ✅ Data loads without errors
- ✅ Visualizations render properly
- ✅ Documentation accessible

### **Performance Targets**
- **Startup Time**: <30 seconds for all services
- **API Response**: <500ms for data endpoints
- **Memory Usage**: <2GB total for all services
- **CPU Usage**: <50% under normal load

---

**🚀 Your project is now fully deployable with both REST API and FastAPI support!**

**Next Steps:**
1. Run `./deploy.sh` or `deploy.bat` to start all services
2. Access the dashboards at the provided URLs
3. Explore the API documentation
4. Monitor performance and logs
5. Scale as needed for production use 