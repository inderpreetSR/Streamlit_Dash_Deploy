@echo off
setlocal enabledelayedexpansion

REM Streamlit & Dash Insights Project - Windows Deployment Script

echo.
echo ========================================
echo 🚀 Streamlit & Dash Insights Project
echo ========================================
echo.

REM Check if Docker is installed
echo [INFO] Checking Docker installation...
docker --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Docker is not installed. Please install Docker Desktop first.
    pause
    exit /b 1
)

docker-compose --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Docker Compose is not installed. Please install Docker Compose first.
    pause
    exit /b 1
)

echo [SUCCESS] Docker and Docker Compose are installed

REM Check if data file exists
echo [INFO] Checking data file...
if not exist "Data\raw\test.csv" (
    echo [WARNING] Data file not found at Data\raw\test.csv
    echo [INFO] Please ensure your data file is placed in Data\raw\test.csv
    set /p continue="Do you want to continue without data? (y/N): "
    if /i not "!continue!"=="y" (
        echo [ERROR] Deployment cancelled
        pause
        exit /b 1
    )
) else (
    echo [SUCCESS] Data file found
)

REM Build and start services
echo [INFO] Building and starting services...

REM Stop any existing containers
docker-compose down --remove-orphans

REM Build images
echo [INFO] Building Docker images...
docker-compose build --no-cache

REM Start services
echo [INFO] Starting services...
docker-compose up -d

echo [SUCCESS] Services started successfully

REM Wait for services to be ready
echo [INFO] Waiting for services to be ready...

REM Wait for Streamlit
echo [INFO] Waiting for Streamlit...
:wait_streamlit
timeout /t 2 /nobreak >nul
curl -s http://localhost:8501 >nul 2>&1
if errorlevel 1 (
    echo [INFO] Still waiting for Streamlit...
    goto wait_streamlit
)

REM Wait for Dash
echo [INFO] Waiting for Dash...
:wait_dash
timeout /t 2 /nobreak >nul
curl -s http://localhost:8050 >nul 2>&1
if errorlevel 1 (
    echo [INFO] Still waiting for Dash...
    goto wait_dash
)

REM Wait for REST API
echo [INFO] Waiting for REST API...
:wait_rest
timeout /t 2 /nobreak >nul
curl -s http://localhost:5000 >nul 2>&1
if errorlevel 1 (
    echo [INFO] Still waiting for REST API...
    goto wait_rest
)

REM Wait for FastAPI
echo [INFO] Waiting for FastAPI...
:wait_fastapi
timeout /t 2 /nobreak >nul
curl -s http://localhost:8000 >nul 2>&1
if errorlevel 1 (
    echo [INFO] Still waiting for FastAPI...
    goto wait_fastapi
)

echo [SUCCESS] All services are ready

REM Display service information
echo.
echo [SUCCESS] 🎉 Deployment Complete!
echo.
echo 📊 Available Services:
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo 🌐 Streamlit Dashboard:  http://localhost:8501
echo 📈 Dash Dashboard:       http://localhost:8050
echo 🔗 REST API:            http://localhost:5000
echo ⚡ FastAPI:             http://localhost:8000
echo 📚 FastAPI Docs:        http://localhost:8000/docs
echo 📖 FastAPI ReDoc:       http://localhost:8000/redoc
echo.
echo 🔧 Management Commands:
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo View logs:              docker-compose logs -f
echo Stop services:          docker-compose down
echo Restart services:       docker-compose restart
echo Update services:        docker-compose pull ^&^& docker-compose up -d
echo.
echo 📋 API Endpoints:
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo REST API Health:        http://localhost:5000/api/health
echo FastAPI Health:         http://localhost:8000/health
echo Data Info:              http://localhost:5000/api/data/info
echo Sample Data:            http://localhost:5000/api/data/sample
echo Gender Analysis:        http://localhost:5000/api/analysis/gender
echo Income Analysis:        http://localhost:5000/api/analysis/income
echo Loan Analysis:          http://localhost:5000/api/analysis/loan
echo.

echo [SUCCESS] Deployment completed successfully!
pause 