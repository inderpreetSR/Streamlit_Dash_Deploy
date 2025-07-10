"""
REST API for Streamlit & Dash Insights Project
Traditional RESTful endpoints using Flask
"""

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import pandas as pd
import json
import os
from pathlib import Path
import sys

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from utils.data_analyzer import FinancialDataAnalyzer
from utils.data_loader import DataLoader
from config.settings import *

try:
    from src.config.settings import DEBUG_MODE
except ImportError:
    DEBUG_MODE = False

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize components
data_loader = DataLoader()
analyzer = FinancialDataAnalyzer()

@app.route('/')
def home():
    """Home endpoint with API information"""
    return jsonify({
        "message": "Streamlit & Dash Insights REST API",
        "version": "1.0.0",
        "endpoints": {
            "data": "/api/data",
            "analysis": "/api/analysis",
            "metrics": "/api/metrics",
            "health": "/api/health"
        }
    })

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": pd.Timestamp.now().isoformat(),
        "data_available": os.path.exists(analyzer.data_path)
    })

@app.route('/api/data/info')
def get_data_info():
    """Get basic information about the dataset"""
    try:
        if not analyzer.df is not None:
            analyzer.load_data(sample_size=1000)
        
        info = analyzer.get_basic_info()
        return jsonify({
            "success": True,
            "data": info
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/data/sample')
def get_data_sample():
    """Get a sample of the data"""
    try:
        sample_size = request.args.get('size', 100, type=int)
        
        if analyzer.df is None:
            analyzer.load_data(sample_size=sample_size)
        
        sample_data = analyzer.df.head(sample_size).to_dict('records')
        
        return jsonify({
            "success": True,
            "data": sample_data,
            "sample_size": len(sample_data)
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/analysis/gender')
def analyze_gender():
    """Analyze gender distribution"""
    try:
        if analyzer.df is None:
            analyzer.load_data(sample_size=1000)
        
        gender_analysis = analyzer.analyze_gender_distribution()
        
        return jsonify({
            "success": True,
            "data": gender_analysis
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/analysis/income')
def analyze_income():
    """Analyze income distribution"""
    try:
        if analyzer.df is None:
            analyzer.load_data(sample_size=1000)
        
        income_analysis = analyzer.analyze_income_distribution()
        
        return jsonify({
            "success": True,
            "data": income_analysis
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/analysis/loan')
def analyze_loan():
    """Analyze loan amounts"""
    try:
        if analyzer.df is None:
            analyzer.load_data(sample_size=1000)
        
        loan_analysis = analyzer.analyze_loan_amounts()
        
        return jsonify({
            "success": True,
            "data": loan_analysis
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/metrics/summary')
def get_summary_metrics():
    """Get summary metrics for dashboard"""
    try:
        if analyzer.df is None:
            analyzer.load_data(sample_size=1000)
        
        metrics = analyzer.create_summary_metrics()
        
        return jsonify({
            "success": True,
            "data": metrics
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/data/columns')
def get_columns():
    """Get list of available columns"""
    try:
        if analyzer.df is None:
            analyzer.load_data(sample_size=1000)
        
        columns = list(analyzer.df.columns)
        
        return jsonify({
            "success": True,
            "data": {
                "columns": columns,
                "total_columns": len(columns)
            }
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/data/filter', methods=['POST'])
def filter_data():
    """Filter data based on criteria"""
    try:
        data = request.get_json()
        column = data.get('column')
        value = data.get('value')
        operator = data.get('operator', 'equals')  # equals, contains, greater_than, less_than
        
        if analyzer.df is None:
            analyzer.load_data(sample_size=1000)
        
        if column not in analyzer.df.columns:
            return jsonify({
                "success": False,
                "error": f"Column '{column}' not found"
            }), 400
        
        # Apply filter
        if operator == 'equals':
            filtered_df = analyzer.df[analyzer.df[column] == value]
        elif operator == 'contains':
            filtered_df = analyzer.df[analyzer.df[column].astype(str).str.contains(str(value), na=False)]
        elif operator == 'greater_than':
            filtered_df = analyzer.df[analyzer.df[column] > value]
        elif operator == 'less_than':
            filtered_df = analyzer.df[analyzer.df[column] < value]
        else:
            return jsonify({
                "success": False,
                "error": f"Invalid operator: {operator}"
            }), 400
        
        filtered_data = filtered_df.head(100).to_dict('records')
        
        return jsonify({
            "success": True,
            "data": {
                "records": filtered_data,
                "total_filtered": len(filtered_df),
                "total_original": len(analyzer.df)
            }
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/export/csv')
def export_csv():
    """Export filtered data as CSV"""
    try:
        sample_size = request.args.get('size', 1000, type=int)
        
        if analyzer.df is None:
            analyzer.load_data(sample_size=sample_size)
        
        # Create temporary file
        export_path = Path(DATA_DIR) / "results" / "export.csv"
        export_path.parent.mkdir(exist_ok=True)
        
        analyzer.df.head(sample_size).to_csv(export_path, index=False)
        
        return send_file(
            export_path,
            as_attachment=True,
            download_name=f"financial_data_export_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
        )
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        "success": False,
        "error": "Endpoint not found",
        "available_endpoints": [
            "/",
            "/api/health",
            "/api/data/info",
            "/api/data/sample",
            "/api/analysis/gender",
            "/api/analysis/income",
            "/api/analysis/loan",
            "/api/metrics/summary",
            "/api/data/columns",
            "/api/data/filter",
            "/api/export/csv"
        ]
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        "success": False,
        "error": "Internal server error"
    }), 500

if __name__ == '__main__':
    print("Starting REST API server...")
    print(f"API will be available at: http://localhost:{REST_API_PORT}")
    print("Available endpoints:")
    print("  GET  / - API information")
    print("  GET  /api/health - Health check")
    print("  GET  /api/data/info - Dataset information")
    print("  GET  /api/data/sample - Data sample")
    print("  GET  /api/analysis/gender - Gender analysis")
    print("  GET  /api/analysis/income - Income analysis")
    print("  GET  /api/analysis/loan - Loan analysis")
    print("  GET  /api/metrics/summary - Summary metrics")
    print("  GET  /api/data/columns - Available columns")
    print("  POST /api/data/filter - Filter data")
    print("  GET  /api/export/csv - Export data")
    
    app.run(
        host=REST_API_HOST,
        port=REST_API_PORT,
        debug=DEBUG_MODE
    ) 