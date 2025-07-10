"""
Unit tests for data loader utilities
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import tempfile
import os

# Import the module to test
import sys
sys.path.append(str(Path(__file__).parent.parent / "src"))
from utils.data_loader import DataLoader, load_csv, save_csv, get_data_summary

class TestDataLoader:
    """Test cases for DataLoader class"""
    
    def setup_method(self):
        """Set up test fixtures"""
        self.temp_dir = tempfile.mkdtemp()
        self.loader = DataLoader(self.temp_dir)
        self.sample_data = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': ['a', 'b', 'c', 'd', 'e'],
            'C': [1.1, 2.2, 3.3, 4.4, 5.5]
        })
    
    def teardown_method(self):
        """Clean up test fixtures"""
        import shutil
        shutil.rmtree(self.temp_dir)
    
    def test_load_csv(self):
        """Test loading CSV file"""
        # Create a temporary CSV file
        csv_path = Path(self.temp_dir) / "test.csv"
        self.sample_data.to_csv(csv_path, index=False)
        
        # Load the data
        loaded_data = self.loader.load_data(csv_path)
        
        # Assertions
        assert isinstance(loaded_data, pd.DataFrame)
        assert loaded_data.shape == self.sample_data.shape
        assert list(loaded_data.columns) == list(self.sample_data.columns)
        pd.testing.assert_frame_equal(loaded_data, self.sample_data)
    
    def test_save_csv(self):
        """Test saving CSV file"""
        csv_path = Path(self.temp_dir) / "output.csv"
        
        # Save the data
        self.loader.save_data(self.sample_data, csv_path)
        
        # Check if file exists
        assert csv_path.exists()
        
        # Load and verify
        loaded_data = pd.read_csv(csv_path)
        pd.testing.assert_frame_equal(loaded_data, self.sample_data)
    
    def test_get_data_info(self):
        """Test getting data information"""
        info = self.loader.get_data_info(self.sample_data)
        
        # Assertions
        assert info['shape'] == (5, 3)
        assert info['columns'] == ['A', 'B', 'C']
        assert info['missing_values']['A'] == 0
        assert info['duplicates'] == 0
        assert 'A' in info['numeric_columns']
        assert 'B' in info['categorical_columns']
    
    def test_clean_data_remove_duplicates(self):
        """Test data cleaning with duplicate removal"""
        # Create data with duplicates
        data_with_duplicates = pd.concat([self.sample_data, self.sample_data.iloc[0:2]])
        
        cleaned_data = self.loader.clean_data(data_with_duplicates, remove_duplicates=True)
        
        assert len(cleaned_data) == len(self.sample_data)
    
    def test_clean_data_handle_missing(self):
        """Test data cleaning with missing values"""
        # Create data with missing values
        data_with_missing = self.sample_data.copy()
        data_with_missing.loc[0, 'A'] = np.nan
        data_with_missing.loc[1, 'B'] = None
        
        # Test drop missing
        cleaned_drop = self.loader.clean_data(data_with_missing, handle_missing='drop')
        assert len(cleaned_drop) < len(data_with_missing)
        
        # Test fill missing
        cleaned_fill = self.loader.clean_data(data_with_missing, handle_missing='fill')
        assert len(cleaned_fill) == len(data_with_missing)
        assert not cleaned_fill.isnull().any().any()
    
    def test_sample_data(self):
        """Test data sampling"""
        # Test sample size
        sampled = self.loader.sample_data(self.sample_data, sample_size=3)
        assert len(sampled) == 3
        
        # Test sample fraction
        sampled = self.loader.sample_data(self.sample_data, sample_fraction=0.6)
        assert len(sampled) == 3  # 5 * 0.6 = 3
    
    def test_generate_sample_data(self):
        """Test sample data generation"""
        generated_data = self.loader.generate_sample_data(rows=100, columns=3)
        
        assert len(generated_data) == 100
        assert len(generated_data.columns) == 3
        assert 'feature_1' in generated_data.columns
        assert 'category' in generated_data.columns

class TestConvenienceFunctions:
    """Test cases for convenience functions"""
    
    def setup_method(self):
        """Set up test fixtures"""
        self.temp_dir = tempfile.mkdtemp()
        self.sample_data = pd.DataFrame({
            'A': [1, 2, 3],
            'B': ['a', 'b', 'c']
        })
    
    def teardown_method(self):
        """Clean up test fixtures"""
        import shutil
        shutil.rmtree(self.temp_dir)
    
    def test_load_csv_function(self):
        """Test load_csv convenience function"""
        csv_path = Path(self.temp_dir) / "test.csv"
        self.sample_data.to_csv(csv_path, index=False)
        
        loaded_data = load_csv(csv_path)
        pd.testing.assert_frame_equal(loaded_data, self.sample_data)
    
    def test_save_csv_function(self):
        """Test save_csv convenience function"""
        csv_path = Path(self.temp_dir) / "output.csv"
        
        save_csv(self.sample_data, csv_path)
        assert csv_path.exists()
        
        loaded_data = pd.read_csv(csv_path)
        pd.testing.assert_frame_equal(loaded_data, self.sample_data)
    
    def test_get_data_summary_function(self):
        """Test get_data_summary convenience function"""
        summary = get_data_summary(self.sample_data)
        
        assert summary['shape'] == (3, 2)
        assert summary['columns'] == ['A', 'B']

if __name__ == "__main__":
    pytest.main([__file__]) 