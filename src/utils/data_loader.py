"""
Data loading and processing utilities
"""

import pandas as pd
import numpy as np
from pathlib import Path
import logging
from typing import Union, Optional, Dict, Any
import json
import pickle
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataLoader:
    """Utility class for loading and processing data files"""
    
    def __init__(self, data_dir: Union[str, Path] = None):
        """
        Initialize DataLoader
        
        Args:
            data_dir: Directory containing data files
        """
        self.data_dir = Path(data_dir) if data_dir else Path("Data")
        self.supported_formats = ['.csv', '.xlsx', '.xls', '.json', '.parquet', '.pkl']
    
    def load_data(self, file_path: Union[str, Path], **kwargs) -> pd.DataFrame:
        """
        Load data from various file formats
        
        Args:
            file_path: Path to the data file
            **kwargs: Additional arguments for pandas read functions
            
        Returns:
            Loaded DataFrame
        """
        file_path = Path(file_path)
        
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        file_extension = file_path.suffix.lower()
        
        try:
            if file_extension == '.csv':
                return pd.read_csv(file_path, **kwargs)
            elif file_extension in ['.xlsx', '.xls']:
                return pd.read_excel(file_path, **kwargs)
            elif file_extension == '.json':
                return pd.read_json(file_path, **kwargs)
            elif file_extension == '.parquet':
                return pd.read_parquet(file_path, **kwargs)
            elif file_extension == '.pkl':
                return pd.read_pickle(file_path, **kwargs)
            else:
                raise ValueError(f"Unsupported file format: {file_extension}")
                
        except Exception as e:
            logger.error(f"Error loading file {file_path}: {str(e)}")
            raise
    
    def save_data(self, data: pd.DataFrame, file_path: Union[str, Path], **kwargs) -> None:
        """
        Save DataFrame to various file formats
        
        Args:
            data: DataFrame to save
            file_path: Path where to save the file
            **kwargs: Additional arguments for pandas write functions
        """
        file_path = Path(file_path)
        file_extension = file_path.suffix.lower()
        
        # Create directory if it doesn't exist
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            if file_extension == '.csv':
                data.to_csv(file_path, index=False, **kwargs)
            elif file_extension in ['.xlsx', '.xls']:
                data.to_excel(file_path, index=False, **kwargs)
            elif file_extension == '.json':
                data.to_json(file_path, orient='records', **kwargs)
            elif file_extension == '.parquet':
                data.to_parquet(file_path, index=False, **kwargs)
            elif file_extension == '.pkl':
                data.to_pickle(file_path, **kwargs)
            else:
                raise ValueError(f"Unsupported file format: {file_extension}")
                
            logger.info(f"Data saved successfully to {file_path}")
            
        except Exception as e:
            logger.error(f"Error saving file {file_path}: {str(e)}")
            raise
    
    def get_data_info(self, data: pd.DataFrame) -> Dict[str, Any]:
        """
        Get comprehensive information about a DataFrame
        
        Args:
            data: DataFrame to analyze
            
        Returns:
            Dictionary containing data information
        """
        info = {
            'shape': data.shape,
            'columns': list(data.columns),
            'dtypes': data.dtypes.to_dict(),
            'missing_values': data.isnull().sum().to_dict(),
            'missing_percentage': (data.isnull().sum() / len(data) * 100).to_dict(),
            'numeric_columns': list(data.select_dtypes(include=[np.number]).columns),
            'categorical_columns': list(data.select_dtypes(include=['object']).columns),
            'datetime_columns': list(data.select_dtypes(include=['datetime']).columns),
            'memory_usage': data.memory_usage(deep=True).sum(),
            'duplicates': data.duplicated().sum()
        }
        
        return info
    
    def clean_data(self, data: pd.DataFrame, 
                   remove_duplicates: bool = True,
                   handle_missing: str = 'drop') -> pd.DataFrame:
        """
        Basic data cleaning operations
        
        Args:
            data: DataFrame to clean
            remove_duplicates: Whether to remove duplicate rows
            handle_missing: How to handle missing values ('drop', 'fill', 'interpolate')
            
        Returns:
            Cleaned DataFrame
        """
        cleaned_data = data.copy()
        
        # Remove duplicates
        if remove_duplicates:
            initial_rows = len(cleaned_data)
            cleaned_data = cleaned_data.drop_duplicates()
            removed_duplicates = initial_rows - len(cleaned_data)
            logger.info(f"Removed {removed_duplicates} duplicate rows")
        
        # Handle missing values
        if handle_missing == 'drop':
            cleaned_data = cleaned_data.dropna()
        elif handle_missing == 'fill':
            # Fill numeric columns with median, categorical with mode
            for col in cleaned_data.columns:
                if cleaned_data[col].dtype in ['int64', 'float64']:
                    cleaned_data[col] = cleaned_data[col].fillna(cleaned_data[col].median())
                else:
                    cleaned_data[col] = cleaned_data[col].fillna(cleaned_data[col].mode()[0] if len(cleaned_data[col].mode()) > 0 else 'Unknown')
        elif handle_missing == 'interpolate':
            cleaned_data = cleaned_data.interpolate()
        
        logger.info(f"Data cleaning completed. Shape: {cleaned_data.shape}")
        return cleaned_data
    
    def sample_data(self, data: pd.DataFrame, 
                   sample_size: Optional[int] = None, 
                   sample_fraction: Optional[float] = None,
                   random_state: int = 42) -> pd.DataFrame:
        """
        Create a sample of the data
        
        Args:
            data: DataFrame to sample
            sample_size: Number of rows to sample
            sample_fraction: Fraction of data to sample (0-1)
            random_state: Random seed for reproducibility
            
        Returns:
            Sampled DataFrame
        """
        if sample_size is not None:
            return data.sample(n=min(sample_size, len(data)), random_state=random_state)
        elif sample_fraction is not None:
            return data.sample(frac=sample_fraction, random_state=random_state)
        else:
            return data
    
    def generate_sample_data(self, rows: int = 1000, 
                           columns: int = 5,
                           include_dates: bool = True) -> pd.DataFrame:
        """
        Generate sample data for testing and development
        
        Args:
            rows: Number of rows to generate
            columns: Number of columns to generate
            include_dates: Whether to include date column
            
        Returns:
            Generated sample DataFrame
        """
        np.random.seed(42)
        
        data = {}
        
        # Generate numeric columns
        for i in range(columns - 1):
            data[f'feature_{i+1}'] = np.random.randn(rows)
        
        # Generate categorical column
        categories = ['A', 'B', 'C', 'D', 'E']
        data['category'] = np.random.choice(categories, rows)
        
        # Generate date column if requested
        if include_dates:
            start_date = datetime(2024, 1, 1)
            dates = [start_date + pd.Timedelta(days=i) for i in range(rows)]
            data['date'] = dates
        
        df = pd.DataFrame(data)
        logger.info(f"Generated sample data with shape: {df.shape}")
        return df

# Convenience functions
def load_csv(file_path: Union[str, Path], **kwargs) -> pd.DataFrame:
    """Load CSV file"""
    loader = DataLoader()
    return loader.load_data(file_path, **kwargs)

def save_csv(data: pd.DataFrame, file_path: Union[str, Path], **kwargs) -> None:
    """Save DataFrame to CSV"""
    loader = DataLoader()
    loader.save_data(data, file_path, **kwargs)

def get_data_summary(data: pd.DataFrame) -> Dict[str, Any]:
    """Get data summary"""
    loader = DataLoader()
    return loader.get_data_info(data) 