"""
Data Analyzer for Financial/Loan Application Dataset
Specialized utilities for analyzing the test.csv dataset
"""

import pandas as pd
import numpy as np
from pathlib import Path
import logging
from typing import Dict, List, Tuple, Any
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FinancialDataAnalyzer:
    """Analyzer for financial/loan application data"""
    
    def __init__(self, data_path: str = "Data/raw/test.csv"):
        """
        Initialize the analyzer
        
        Args:
            data_path: Path to the CSV file
        """
        self.data_path = Path(data_path)
        self.df = None
        self.analysis_results = {}
        
    def load_data(self, sample_size: int = None) -> pd.DataFrame:
        """
        Load the financial data
        
        Args:
            sample_size: Number of rows to load (for testing)
            
        Returns:
            Loaded DataFrame
        """
        try:
            if sample_size:
                self.df = pd.read_csv(self.data_path, nrows=sample_size)
                logger.info(f"Loaded {sample_size} rows from {self.data_path}")
            else:
                self.df = pd.read_csv(self.data_path)
                logger.info(f"Loaded full dataset: {len(self.df)} rows from {self.data_path}")
            
            return self.df
            
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
    
    def get_basic_info(self) -> Dict[str, Any]:
        """
        Get basic information about the dataset
        
        Returns:
            Dictionary with basic dataset information
        """
        if self.df is None:
            self.load_data(sample_size=1000)  # Load sample for analysis
            
        info = {
            'total_rows': len(self.df),
            'total_columns': len(self.df.columns),
            'memory_usage_mb': self.df.memory_usage(deep=True).sum() / 1024 / 1024,
            'missing_values': self.df.isnull().sum().sum(),
            'duplicate_rows': self.df.duplicated().sum(),
            'column_categories': {
                'personal_info': self._get_personal_info_columns(),
                'financial_info': self._get_financial_info_columns(),
                'address_info': self._get_address_info_columns(),
                'employment_info': self._get_employment_info_columns(),
                'loan_info': self._get_loan_info_columns()
            }
        }
        
        return info
    
    def _get_personal_info_columns(self) -> List[str]:
        """Get personal information columns"""
        personal_keywords = ['NAME', 'GENDER', 'AGE', 'BIRTH', 'MARITAL', 'EDUCATION', 'QUALIFICATION']
        return [col for col in self.df.columns if any(keyword in col.upper() for keyword in personal_keywords)]
    
    def _get_financial_info_columns(self) -> List[str]:
        """Get financial information columns"""
        financial_keywords = ['INCOME', 'SALARY', 'AMOUNT', 'VALUE', 'WORTH', 'BANK', 'ACCOUNT']
        return [col for col in self.df.columns if any(keyword in col.upper() for keyword in financial_keywords)]
    
    def _get_address_info_columns(self) -> List[str]:
        """Get address information columns"""
        address_keywords = ['ADDRESS', 'CITY', 'STATE', 'PIN', 'LOCATION', 'LATITUDE', 'LONGITUDE']
        return [col for col in self.df.columns if any(keyword in col.upper() for keyword in address_keywords)]
    
    def _get_employment_info_columns(self) -> List[str]:
        """Get employment information columns"""
        employment_keywords = ['EMPLOYMENT', 'EMPLOYER', 'EXPERIENCE', 'DESIGNATION', 'BUSINESS', 'OCCUPATION']
        return [col for col in self.df.columns if any(keyword in col.upper() for keyword in employment_keywords)]
    
    def _get_loan_info_columns(self) -> List[str]:
        """Get loan information columns"""
        loan_keywords = ['LOAN', 'APPLICATION', 'DISBURSED', 'AMOUNT', 'RATE', 'STATUS', 'APPROVED']
        return [col for col in self.df.columns if any(keyword in col.upper() for keyword in loan_keywords)]
    
    def analyze_gender_distribution(self) -> Dict[str, Any]:
        """Analyze gender distribution"""
        if 'GENDER' in self.df.columns:
            gender_counts = self.df['GENDER'].value_counts()
            gender_percentages = (gender_counts / len(self.df) * 100).round(2)
            
            return {
                'counts': gender_counts.to_dict(),
                'percentages': gender_percentages.to_dict(),
                'total': len(self.df)
            }
        return {}
    
    def analyze_income_distribution(self) -> Dict[str, Any]:
        """Analyze income distribution"""
        income_columns = [col for col in self.df.columns if 'INCOME' in col.upper()]
        
        results = {}
        for col in income_columns:
            if self.df[col].dtype in ['int64', 'float64']:
                results[col] = {
                    'mean': self.df[col].mean(),
                    'median': self.df[col].median(),
                    'std': self.df[col].std(),
                    'min': self.df[col].min(),
                    'max': self.df[col].max(),
                    'missing': self.df[col].isnull().sum()
                }
        
        return results
    
    def analyze_loan_amounts(self) -> Dict[str, Any]:
        """Analyze loan amounts"""
        amount_columns = [col for col in self.df.columns if 'AMOUNT' in col.upper()]
        
        results = {}
        for col in amount_columns:
            if self.df[col].dtype in ['int64', 'float64']:
                results[col] = {
                    'mean': self.df[col].mean(),
                    'median': self.df[col].median(),
                    'std': self.df[col].std(),
                    'min': self.df[col].min(),
                    'max': self.df[col].max(),
                    'total': self.df[col].sum(),
                    'missing': self.df[col].isnull().sum()
                }
        
        return results
    
    def analyze_application_status(self) -> Dict[str, Any]:
        """Analyze application status"""
        status_columns = [col for col in self.df.columns if 'STATUS' in col.upper()]
        
        results = {}
        for col in status_columns:
            if self.df[col].dtype == 'object':
                status_counts = self.df[col].value_counts()
                results[col] = {
                    'counts': status_counts.to_dict(),
                    'percentages': (status_counts / len(self.df) * 100).round(2).to_dict()
                }
        
        return results
    
    def analyze_geographic_distribution(self) -> Dict[str, Any]:
        """Analyze geographic distribution"""
        results = {}
        
        # State distribution
        if 'ADDRESS_STATE_CODE' in self.df.columns:
            state_counts = self.df['ADDRESS_STATE_CODE'].value_counts().head(10)
            results['states'] = {
                'top_10': state_counts.to_dict(),
                'total_states': self.df['ADDRESS_STATE_CODE'].nunique()
            }
        
        # City distribution
        if 'ADDRESS_CITY_CODE' in self.df.columns:
            city_counts = self.df['ADDRESS_CITY_CODE'].value_counts().head(10)
            results['cities'] = {
                'top_10': city_counts.to_dict(),
                'total_cities': self.df['ADDRESS_CITY_CODE'].nunique()
            }
        
        return results
    
    def create_summary_metrics(self) -> Dict[str, Any]:
        """Create summary metrics for dashboard"""
        if self.df is None:
            self.load_data(sample_size=1000)
        
        metrics = {
            'total_applications': len(self.df),
            'total_columns': len(self.df.columns),
            'data_size_mb': round(self.df.memory_usage(deep=True).sum() / 1024 / 1024, 2),
            'missing_data_percentage': round(self.df.isnull().sum().sum() / (len(self.df) * len(self.df.columns)) * 100, 2)
        }
        
        # Add financial metrics if available
        amount_columns = [col for col in self.df.columns if 'AMOUNT' in col.upper()]
        if amount_columns:
            total_amount = 0
            for col in amount_columns:
                if self.df[col].dtype in ['int64', 'float64']:
                    total_amount += self.df[col].sum()
            metrics['total_amount'] = round(total_amount, 2)
        
        return metrics
    
    def generate_sample_visualizations(self) -> Dict[str, Any]:
        """Generate sample visualizations for the dashboard"""
        if self.df is None:
            self.load_data(sample_size=1000)
        
        viz_data = {}
        
        # Gender distribution pie chart
        if 'GENDER' in self.df.columns:
            gender_counts = self.df['GENDER'].value_counts()
            viz_data['gender_distribution'] = {
                'labels': gender_counts.index.tolist(),
                'values': gender_counts.values.tolist()
            }
        
        # Income distribution histogram
        income_columns = [col for col in self.df.columns if 'INCOME' in col.upper()]
        if income_columns:
            for col in income_columns:
                if self.df[col].dtype in ['int64', 'float64']:
                    viz_data['income_distribution'] = {
                        'column': col,
                        'values': self.df[col].dropna().tolist()
                    }
                    break
        
        # Application status bar chart
        status_columns = [col for col in self.df.columns if 'STATUS' in col.upper()]
        if status_columns:
            for col in status_columns:
                if self.df[col].dtype == 'object':
                    status_counts = self.df[col].value_counts().head(10)
                    viz_data['application_status'] = {
                        'labels': status_counts.index.tolist(),
                        'values': status_counts.values.tolist()
                    }
                    break
        
        return viz_data
    
    def get_column_summary(self) -> Dict[str, Any]:
        """Get summary of all columns"""
        if self.df is None:
            self.load_data(sample_size=1000)
        
        summary = {}
        for col in self.df.columns:
            col_info = {
                'dtype': str(self.df[col].dtype),
                'missing_count': self.df[col].isnull().sum(),
                'missing_percentage': round(self.df[col].isnull().sum() / len(self.df) * 100, 2),
                'unique_values': self.df[col].nunique()
            }
            
            if self.df[col].dtype in ['int64', 'float64']:
                col_info.update({
                    'mean': self.df[col].mean(),
                    'median': self.df[col].median(),
                    'std': self.df[col].std(),
                    'min': self.df[col].min(),
                    'max': self.df[col].max()
                })
            else:
                col_info['top_values'] = self.df[col].value_counts().head(5).to_dict()
            
            summary[col] = col_info
        
        return summary

# Convenience functions
def analyze_financial_data(data_path: str = "Data/raw/test.csv", sample_size: int = None) -> FinancialDataAnalyzer:
    """Convenience function to analyze financial data"""
    analyzer = FinancialDataAnalyzer(data_path)
    analyzer.load_data(sample_size)
    return analyzer

def get_dashboard_metrics(data_path: str = "Data/raw/test.csv") -> Dict[str, Any]:
    """Get metrics for dashboard display"""
    analyzer = FinancialDataAnalyzer(data_path)
    analyzer.load_data(sample_size=1000)
    return analyzer.create_summary_metrics()

def get_visualization_data(data_path: str = "Data/raw/test.csv") -> Dict[str, Any]:
    """Get data for visualizations"""
    analyzer = FinancialDataAnalyzer(data_path)
    analyzer.load_data(sample_size=1000)
    return analyzer.generate_sample_visualizations() 