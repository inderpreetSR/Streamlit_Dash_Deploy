# Internal Paths & Code Communication Learning Resource

## Overview
Managing file paths and inter-module communication is crucial for scalable, maintainable projects. Python provides several modules (os, pathlib, config) to handle paths, environment variables, and cross-module imports.

## Key Concepts & Glossary
- **os**: Standard library for interacting with the operating system (paths, environment, etc.)
- **pathlib**: Modern, object-oriented path handling
- **sys.path**: List of directories Python searches for modules
- **PYTHONPATH**: Environment variable to add custom module search paths
- **Configuration Module**: Central place for settings (e.g., src/config/settings.py)

## Syntax & Examples
```python
# Using os for paths
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, '../../Data/raw/test.csv')

# Using pathlib
from pathlib import Path
base_dir = Path(__file__).resolve().parent
results_dir = base_dir / '../../Data/results/'

# Using config for central settings
from src.config import settings
print(settings.DATA_DIR)

# Setting PYTHONPATH (in Docker or shell)
export PYTHONPATH=/app
```

## Common Use Cases
- Loading and saving data files
- Storing results and logs
- Sharing configuration across modules
- Importing utilities from different directories

## Setup & Usage
- Use `os` or `pathlib` for robust, cross-platform path handling
- Centralize paths in a config/settings module
- Set `PYTHONPATH` in Docker or environment for custom imports

## Best Practices
- Avoid hardcoding absolute paths; use relative paths and config
- Use `pathlib` for new code (more readable and powerful)
- Store all directory paths in a single config file
- Use environment variables for secrets and deployment-specific paths

## External Learning Links
- [Python os module](https://docs.python.org/3/library/os.html)
- [Python pathlib module](https://docs.python.org/3/library/pathlib.html)
- [Managing Python Paths and Imports](https://realpython.com/python-modules-packages/)
- [Best Practices for Project Structure](https://realpython.com/python-application-layouts/)

## How it is Used in This Project
- All data, results, and logs paths are managed via `src/config/settings.py`
- Utility modules (`data_loader.py`, `data_analyzer.py`) use config paths for file operations
- Docker sets `PYTHONPATH` to `/app` so all modules are importable
- No hardcoded paths; everything is relative to the project root or config
- Example: `settings.DATA_DIR`, `settings.RESULTS_DIR` are used throughout the codebase for consistency 

## Core Concepts Used in This Project
- Used os and pathlib for cross-platform path management.
- Centralized all paths in src/config/settings.py for consistency.
- Used PYTHONPATH and relative imports for module communication.

## Ignored/Alternative Concepts
- Not used: Hardcoded absolute paths, manual sys.path hacks, or global variables for config.
- Reason: Central config and standard modules are safer and more maintainable.

## Other Concepts You Could Use
- Use environment variables for all paths (12-factor app style)
- Use config libraries like pydantic-settings or dynaconf
- Use importlib.resources for package data

## Technology Foundations
- Built on Python standard library (os, pathlib, sys, importlib).

## Advantages & Disadvantages
**Advantages:**
- Cross-platform and robust
- Easy to update paths in one place
- Reduces bugs from path errors

**Disadvantages:**
- Requires discipline to always use config
- Can be verbose for very simple scripts 

## Project Keywords Used
- os
- pathlib
- os.path.join
- Path(__file__).resolve()
- sys.path
- PYTHONPATH
- src/config/settings.py
- DATA_DIR
- RESULTS_DIR
- Relative imports
- Environment variables 