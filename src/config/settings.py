"""
Configuration settings for the Streamlit and Dash Insights Project
"""

import os
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent

# Data directories
DATA_DIR = PROJECT_ROOT / "Data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"
INTERIM_DATA_DIR = DATA_DIR / "interim"
RESULTS_DIR = DATA_DIR / "results"

# Source directories
SRC_DIR = PROJECT_ROOT / "src"
STREAMLIT_DIR = SRC_DIR / "streamlit"
DASH_DIR = SRC_DIR / "dash"
UTILS_DIR = SRC_DIR / "utils"
MODELS_DIR = SRC_DIR / "models"
COMPONENTS_DIR = SRC_DIR / "components"

# Application settings
APP_NAME = "Data Insights Dashboard"
APP_VERSION = "1.0.0"
DEBUG = True

# Database settings
DATABASE_URL = "sqlite:///data.db"
DATABASE_ECHO = False

# API settings
API_HOST = "0.0.0.0"
API_PORT = 8000
API_DEBUG = True

# REST API settings
REST_API_HOST = "localhost"
REST_API_PORT = 5000

# FastAPI settings
FASTAPI_HOST = "localhost"
FASTAPI_PORT = 8000

# Streamlit settings
STREAMLIT_PORT = 8501
STREAMLIT_HOST = "localhost"

# Dash settings
DASH_PORT = 8050
DASH_HOST = "0.0.0.0"
DASH_DEBUG = True

# Visualization settings
CHART_HEIGHT = 400
CHART_WIDTH = None  # Auto-width
CHART_TEMPLATE = "plotly_white"

# Data processing settings
CHUNK_SIZE = 10000
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB
SUPPORTED_FORMATS = ['.csv', '.xlsx', '.xls', '.json', '.parquet']

# Machine Learning settings
MODEL_DIR = MODELS_DIR
RANDOM_STATE = 42
TEST_SIZE = 0.2
CROSS_VALIDATION_FOLDS = 5

# Logging settings
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = PROJECT_ROOT / "logs" / "app.log"

# Security settings
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

# Cache settings
CACHE_TIMEOUT = 300  # 5 minutes
CACHE_TYPE = "simple"

# Theme settings
DEFAULT_THEME = "light"
AVAILABLE_THEMES = ["light", "dark", "auto"]

# Performance settings
MAX_WORKERS = 4
TIMEOUT = 30

# Create directories if they don't exist
def create_directories():
    """Create necessary directories if they don't exist"""
    directories = [
        DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR, EXTERNAL_DATA_DIR,
        INTERIM_DATA_DIR, RESULTS_DIR, MODELS_DIR, LOG_FILE.parent
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)

# Initialize directories
create_directories() 