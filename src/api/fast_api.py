"""
FastAPI for Streamlit & Dash Insights Project
Modern, high-performance API with automatic documentation
"""

from fastapi import FastAPI, HTTPException, Query, Body, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
import pandas as pd
import uvicorn
from pathlib import Path
import sys
import os

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from utils.data_analyzer import FinancialDataAnalyzer
from utils.data_loader import DataLoader
from config.settings import *

# Initialize FastAPI app
app = FastAPI(
    title="Streamlit & Dash Insights API",
    description="Modern API for financial data analysis and insights",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize components
data_loader = DataLoader()
analyzer = FinancialDataAnalyzer()

# Pydantic models for request/response validation
class FilterRequest(BaseModel):
    column: str = Field(..., description="Column name to filter on")
    value: Any = Field(..., description="Value to filter by")
    operator: str = Field(default="equals", description="Filter operator: equals, contains, greater_than, less_than")

class AnalysisResponse(BaseModel):
    success: bool
    data: Dict[str, Any]
    message: Optional[str] = None

class DataResponse(BaseModel):
    success: bool
    data: List[Dict[str, Any]]
    total_count: int
    sample_size: int

class HealthResponse(BaseModel):
    status: str
    timestamp: str
    data_available: bool
    version: str

# Dependency for analyzer
def get_analyzer():
    """Dependency to get analyzer instance"""
    if analyzer.df is None:
        analyzer.load_data(sample_size=1000)
    return analyzer

@app.get("/", response_model=Dict[str, Any])
async def home():
    """Home endpoint with API information"""
    return {
        "message": "Streamlit & Dash Insights FastAPI",
        "version": "1.0.0",
        "documentation": "/docs",
        "endpoints": {
            "health": "/health",
            "data": "/data",
            "analysis": "/analysis",
            "metrics": "/metrics"
        }
    }

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        timestamp=pd.Timestamp.now().isoformat(),
        data_available=os.path.exists(analyzer.data_path),
        version="1.0.0"
    )

@app.get("/data/info", response_model=AnalysisResponse)
async def get_data_info(analyzer: FinancialDataAnalyzer = Depends(get_analyzer)):
    """Get basic information about the dataset"""
    try:
        info = analyzer.get_basic_info()
        return AnalysisResponse(
            success=True,
            data=info
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/data/sample", response_model=DataResponse)
async def get_data_sample(
    size: int = Query(default=100, ge=1, le=1000, description="Sample size"),
    analyzer: FinancialDataAnalyzer = Depends(get_analyzer)
):
    """Get a sample of the data"""
    try:
        sample_data = analyzer.df.head(size).to_dict('records')
        return DataResponse(
            success=True,
            data=sample_data,
            total_count=len(analyzer.df),
            sample_size=len(sample_data)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/data/columns", response_model=AnalysisResponse)
async def get_columns(analyzer: FinancialDataAnalyzer = Depends(get_analyzer)):
    """Get list of available columns"""
    try:
        columns = list(analyzer.df.columns)
        return AnalysisResponse(
            success=True,
            data={
                "columns": columns,
                "total_columns": len(columns)
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/data/filter", response_model=DataResponse)
async def filter_data(
    filter_request: FilterRequest,
    analyzer: FinancialDataAnalyzer = Depends(get_analyzer)
):
    """Filter data based on criteria"""
    try:
        if filter_request.column not in analyzer.df.columns:
            raise HTTPException(
                status_code=400, 
                detail=f"Column '{filter_request.column}' not found"
            )
        
        # Apply filter
        if filter_request.operator == 'equals':
            filtered_df = analyzer.df[analyzer.df[filter_request.column] == filter_request.value]
        elif filter_request.operator == 'contains':
            filtered_df = analyzer.df[analyzer.df[filter_request.column].astype(str).str.contains(str(filter_request.value), na=False)]
        elif filter_request.operator == 'greater_than':
            filtered_df = analyzer.df[analyzer.df[filter_request.column] > filter_request.value]
        elif filter_request.operator == 'less_than':
            filtered_df = analyzer.df[analyzer.df[filter_request.column] < filter_request.value]
        else:
            raise HTTPException(
                status_code=400, 
                detail=f"Invalid operator: {filter_request.operator}"
            )
        
        filtered_data = filtered_df.head(100).to_dict('records')
        
        return DataResponse(
            success=True,
            data=filtered_data,
            total_count=len(filtered_df),
            sample_size=len(filtered_data)
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/analysis/gender", response_model=AnalysisResponse)
async def analyze_gender(analyzer: FinancialDataAnalyzer = Depends(get_analyzer)):
    """Analyze gender distribution"""
    try:
        gender_analysis = analyzer.analyze_gender_distribution()
        return AnalysisResponse(
            success=True,
            data=gender_analysis
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/analysis/income", response_model=AnalysisResponse)
async def analyze_income(analyzer: FinancialDataAnalyzer = Depends(get_analyzer)):
    """Analyze income distribution"""
    try:
        income_analysis = analyzer.analyze_income_distribution()
        return AnalysisResponse(
            success=True,
            data=income_analysis
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/analysis/loan", response_model=AnalysisResponse)
async def analyze_loan(analyzer: FinancialDataAnalyzer = Depends(get_analyzer)):
    """Analyze loan amounts"""
    try:
        loan_analysis = analyzer.analyze_loan_amounts()
        return AnalysisResponse(
            success=True,
            data=loan_analysis
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/metrics/summary", response_model=AnalysisResponse)
async def get_summary_metrics(analyzer: FinancialDataAnalyzer = Depends(get_analyzer)):
    """Get summary metrics for dashboard"""
    try:
        metrics = analyzer.create_summary_metrics()
        return AnalysisResponse(
            success=True,
            data=metrics
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/export/csv")
async def export_csv(
    size: int = Query(default=1000, ge=1, le=10000, description="Export size"),
    analyzer: FinancialDataAnalyzer = Depends(get_analyzer)
):
    """Export data as CSV"""
    try:
        # Create export file
        export_path = Path(DATA_DIR) / "results" / "export.csv"
        export_path.parent.mkdir(exist_ok=True)
        
        analyzer.df.head(size).to_csv(export_path, index=False)
        
        return FileResponse(
            path=export_path,
            filename=f"financial_data_export_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv",
            media_type='text/csv'
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/stats/performance")
async def get_performance_stats(analyzer: FinancialDataAnalyzer = Depends(get_analyzer)):
    """Get performance statistics"""
    try:
        stats = {
            "total_rows": len(analyzer.df),
            "total_columns": len(analyzer.df.columns),
            "memory_usage_mb": round(analyzer.df.memory_usage(deep=True).sum() / 1024 / 1024, 2),
            "missing_values": analyzer.df.isnull().sum().sum(),
            "duplicate_rows": analyzer.df.duplicated().sum(),
            "data_types": analyzer.df.dtypes.value_counts().to_dict()
        }
        
        return AnalysisResponse(
            success=True,
            data=stats
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/analysis/correlation")
async def get_correlation_matrix(
    columns: Optional[List[str]] = Query(default=None, description="Columns to analyze"),
    analyzer: FinancialDataAnalyzer = Depends(get_analyzer)
):
    """Get correlation matrix for numerical columns"""
    try:
        # Get numerical columns
        numerical_cols = analyzer.df.select_dtypes(include=['number']).columns.tolist()
        
        if columns:
            # Filter to requested columns that are numerical
            columns = [col for col in columns if col in numerical_cols]
        else:
            columns = numerical_cols[:10]  # Limit to first 10 columns
        
        if not columns:
            raise HTTPException(status_code=400, detail="No numerical columns found")
        
        correlation_matrix = analyzer.df[columns].corr().round(3)
        
        return AnalysisResponse(
            success=True,
            data={
                "correlation_matrix": correlation_matrix.to_dict(),
                "columns_analyzed": columns
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Custom exception handlers
@app.exception_handler(404)
async def not_found_handler(request, exc):
    """Handle 404 errors"""
    return JSONResponse(
        status_code=404,
        content={
            "success": False,
            "error": "Endpoint not found",
            "available_endpoints": [
                "/",
                "/health",
                "/data/info",
                "/data/sample",
                "/data/columns",
                "/data/filter",
                "/analysis/gender",
                "/analysis/income",
                "/analysis/loan",
                "/metrics/summary",
                "/export/csv",
                "/stats/performance",
                "/analysis/correlation"
            ]
        }
    )

@app.exception_handler(500)
async def internal_error_handler(request, exc):
    """Handle 500 errors"""
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": "Internal server error"
        }
    )

if __name__ == '__main__':
    print("Starting FastAPI server...")
    print(f"API will be available at: http://localhost:{FASTAPI_PORT}")
    print(f"Interactive documentation: http://localhost:{FASTAPI_PORT}/docs")
    print(f"ReDoc documentation: http://localhost:{FASTAPI_PORT}/redoc")
    print("\nAvailable endpoints:")
    print("  GET  / - API information")
    print("  GET  /health - Health check")
    print("  GET  /data/info - Dataset information")
    print("  GET  /data/sample - Data sample")
    print("  GET  /data/columns - Available columns")
    print("  POST /data/filter - Filter data")
    print("  GET  /analysis/gender - Gender analysis")
    print("  GET  /analysis/income - Income analysis")
    print("  GET  /analysis/loan - Loan analysis")
    print("  GET  /metrics/summary - Summary metrics")
    print("  GET  /export/csv - Export data")
    print("  GET  /stats/performance - Performance statistics")
    print("  GET  /analysis/correlation - Correlation matrix")
    
    uvicorn.run(
        "fast_api:app",
        host=FASTAPI_HOST,
        port=FASTAPI_PORT,
        reload=DEBUG_MODE
    ) 