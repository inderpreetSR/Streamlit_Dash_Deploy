# API Documentation

This document provides comprehensive API documentation for the Streamlit and Dash Insights Project.

## Table of Contents

1. [DataLoader Class](#dataloader-class)
2. [Configuration Settings](#configuration-settings)
3. [Streamlit Application](#streamlit-application)
4. [Dash Application](#dash-application)
5. [Utility Functions](#utility-functions)

## DataLoader Class

The `DataLoader` class provides utilities for loading, saving, and processing data files.

### Constructor

```python
DataLoader(data_dir: Union[str, Path] = None)
```

**Parameters:**
- `data_dir`: Directory containing data files (optional)

### Methods

#### load_data()

```python
load_data(file_path: Union[str, Path], **kwargs) -> pd.DataFrame
```

Loads data from various file formats (CSV, Excel, JSON, Parquet, Pickle).

**Parameters:**
- `file_path`: Path to the data file
- `**kwargs`: Additional arguments for pandas read functions

**Returns:**
- Loaded DataFrame

**Example:**
```python
loader = DataLoader()
df = loader.load_data("data.csv")
```

#### save_data()

```python
save_data(data: pd.DataFrame, file_path: Union[str, Path], **kwargs) -> None
```

Saves DataFrame to various file formats.

**Parameters:**
- `data`: DataFrame to save
- `file_path`: Path where to save the file
- `**kwargs`: Additional arguments for pandas write functions

**Example:**
```python
loader = DataLoader()
loader.save_data(df, "output.csv")
```

#### get_data_info()

```python
get_data_info(data: pd.DataFrame) -> Dict[str, Any]
```

Gets comprehensive information about a DataFrame.

**Parameters:**
- `data`: DataFrame to analyze

**Returns:**
- Dictionary containing data information

**Example:**
```python
info = loader.get_data_info(df)
print(f"Shape: {info['shape']}")
print(f"Missing values: {info['missing_values']}")
```

#### clean_data()

```python
clean_data(data: pd.DataFrame, 
           remove_duplicates: bool = True,
           handle_missing: str = 'drop') -> pd.DataFrame
```

Performs basic data cleaning operations.

**Parameters:**
- `data`: DataFrame to clean
- `remove_duplicates`: Whether to remove duplicate rows (default: True)
- `handle_missing`: How to handle missing values ('drop', 'fill', 'interpolate') (default: 'drop')

**Returns:**
- Cleaned DataFrame

**Example:**
```python
cleaned_df = loader.clean_data(df, handle_missing='fill')
```

#### sample_data()

```python
sample_data(data: pd.DataFrame, 
            sample_size: Optional[int] = None, 
            sample_fraction: Optional[float] = None,
            random_state: int = 42) -> pd.DataFrame
```

Creates a sample of the data.

**Parameters:**
- `data`: DataFrame to sample
- `sample_size`: Number of rows to sample
- `sample_fraction`: Fraction of data to sample (0-1)
- `random_state`: Random seed for reproducibility (default: 42)

**Returns:**
- Sampled DataFrame

**Example:**
```python
sample_df = loader.sample_data(df, sample_size=100)
```

#### generate_sample_data()

```python
generate_sample_data(rows: int = 1000, 
                    columns: int = 5,
                    include_dates: bool = True) -> pd.DataFrame
```

Generates sample data for testing and development.

**Parameters:**
- `rows`: Number of rows to generate (default: 1000)
- `columns`: Number of columns to generate (default: 5)
- `include_dates`: Whether to include date column (default: True)

**Returns:**
- Generated sample DataFrame

**Example:**
```python
sample_data = loader.generate_sample_data(rows=500, columns=3)
```

## Configuration Settings

The configuration module provides centralized settings for the project.

### Key Settings

#### Data Directories
```python
DATA_DIR = PROJECT_ROOT / "Data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"
INTERIM_DATA_DIR = DATA_DIR / "interim"
RESULTS_DIR = DATA_DIR / "results"
```

#### Application Settings
```python
APP_NAME = "Data Insights Dashboard"
APP_VERSION = "1.0.0"
DEBUG = True
```

#### Server Settings
```python
# Streamlit
STREAMLIT_PORT = 8501
STREAMLIT_HOST = "localhost"

# Dash
DASH_PORT = 8050
DASH_HOST = "0.0.0.0"
DASH_DEBUG = True
```

#### Data Processing Settings
```python
CHUNK_SIZE = 10000
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB
SUPPORTED_FORMATS = ['.csv', '.xlsx', '.xls', '.json', '.parquet']
```

## Streamlit Application

The Streamlit application provides an interactive web interface for data analysis.

### Main Functions

#### main()
Main application function that handles navigation and page routing.

#### show_overview()
Displays the dashboard overview with metrics and sample visualizations.

#### show_data_analysis()
Provides data upload and analysis functionality.

#### show_visualizations()
Displays various data visualizations and charts.

#### show_predictions()
Placeholder for machine learning models and predictions.

#### show_settings()
Allows users to configure dashboard settings.

### Usage

```bash
cd src/streamlit
streamlit run app.py
```

## Dash Application

The Dash application provides a more advanced web interface with interactive components.

### Main Components

#### App Layout
- Header with title
- Navigation tabs
- Interactive components
- Bootstrap styling

#### Callbacks

##### update_time_series_chart()
Updates the time series chart with sample data.

##### update_pie_chart()
Updates the pie chart with sample distribution data.

##### update_bar_chart()
Updates the bar chart with sample categorical data.

##### update_scatter_chart()
Updates the scatter plot with sample correlation data.

##### update_output()
Handles file upload and displays data preview.

### Usage

```bash
cd src/dash
python app.py
```

## Utility Functions

### Convenience Functions

#### load_csv()
```python
load_csv(file_path: Union[str, Path], **kwargs) -> pd.DataFrame
```
Loads a CSV file using the DataLoader.

#### save_csv()
```python
save_csv(data: pd.DataFrame, file_path: Union[str, Path], **kwargs) -> None
```
Saves a DataFrame to CSV format.

#### get_data_summary()
```python
get_data_summary(data: pd.DataFrame) -> Dict[str, Any]
```
Gets a summary of data information.

## Error Handling

The API includes comprehensive error handling for:

- File not found errors
- Unsupported file formats
- Data processing errors
- Invalid parameters

## Logging

The application uses Python's logging module with configurable levels:

- INFO: General information
- WARNING: Warning messages
- ERROR: Error messages
- DEBUG: Debug information (when DEBUG=True)

## Performance Considerations

- Large files are processed in chunks (configurable via CHUNK_SIZE)
- Memory usage is optimized for data processing
- Caching is implemented for frequently accessed data
- Async operations are used where appropriate

## Security

- File upload validation
- Path traversal protection
- Input sanitization
- Secure configuration management

## Testing

The project includes comprehensive unit tests:

```bash
pytest tests/
```

For specific test files:
```bash
pytest tests/test_data_loader.py
```

## Contributing

When contributing to the API:

1. Follow the existing code style
2. Add comprehensive docstrings
3. Include unit tests for new functionality
4. Update this documentation
5. Ensure backward compatibility 