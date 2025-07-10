"""
Streamlit Insights Dashboard
Main application file for the Streamlit dashboard
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import our custom utilities
from utils.data_analyzer import FinancialDataAnalyzer, get_dashboard_metrics, get_visualization_data

# Page configuration
st.set_page_config(
    page_title="Data Insights Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
</style>
""", unsafe_allow_html=True)

def main():
    """Main application function"""
    
    # Header
    st.markdown('<h1 class="main-header">📊 Data Insights Dashboard</h1>', unsafe_allow_html=True)
    
    # Sidebar
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Choose a page",
        ["Overview", "Data Analysis", "Visualizations", "Predictions", "Settings"]
    )
    
    # Main content based on page selection
    if page == "Overview":
        show_overview()
    elif page == "Data Analysis":
        show_data_analysis()
    elif page == "Visualizations":
        show_visualizations()
    elif page == "Predictions":
        show_predictions()
    elif page == "Settings":
        show_settings()

def show_overview():
    """Display overview page"""
    st.header("📈 Financial Data Dashboard Overview")
    
    # Load real data metrics
    try:
        metrics = get_dashboard_metrics()
        viz_data = get_visualization_data()
        
        # Display metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(label="Total Applications", value=f"{metrics.get('total_applications', 0):,}")
        
        with col2:
            st.metric(label="Total Columns", value=f"{metrics.get('total_columns', 0):,}")
        
        with col3:
            st.metric(label="Data Size (MB)", value=f"{metrics.get('data_size_mb', 0):.1f}")
        
        with col4:
            st.metric(label="Missing Data %", value=f"{metrics.get('missing_data_percentage', 0):.1f}%")
        
        # Display visualizations
        st.subheader("📊 Data Insights")
        
        # Gender distribution
        if 'gender_distribution' in viz_data:
            col1, col2 = st.columns(2)
            
            with col1:
                fig_gender = px.pie(
                    values=viz_data['gender_distribution']['values'],
                    names=viz_data['gender_distribution']['labels'],
                    title='Gender Distribution'
                )
                st.plotly_chart(fig_gender, use_container_width=True)
        
        # Application status
        if 'application_status' in viz_data:
            with col2:
                fig_status = px.bar(
                    x=viz_data['application_status']['labels'],
                    y=viz_data['application_status']['values'],
                    title='Application Status Distribution'
                )
                st.plotly_chart(fig_status, use_container_width=True)
        
        # Income distribution
        if 'income_distribution' in viz_data:
            st.subheader("Income Distribution")
            fig_income = px.histogram(
                x=viz_data['income_distribution']['values'],
                title=f"Income Distribution - {viz_data['income_distribution']['column']}",
                nbins=20
            )
            st.plotly_chart(fig_income, use_container_width=True)
            
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        st.info("Please ensure the test.csv file is in the Data/raw/ directory")

def show_data_analysis():
    """Display data analysis page"""
    st.header("🔍 Financial Data Analysis")
    
    # Load and analyze the financial data
    try:
        analyzer = FinancialDataAnalyzer()
        analyzer.load_data(sample_size=1000)  # Load sample for analysis
        
        # Basic info
        basic_info = analyzer.get_basic_info()
        
        st.subheader("📋 Dataset Overview")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Rows", f"{basic_info['total_rows']:,}")
        with col2:
            st.metric("Total Columns", f"{basic_info['total_columns']:,}")
        with col3:
            st.metric("Memory Usage", f"{basic_info['memory_usage_mb']:.1f} MB")
        
        # Column categories
        st.subheader("📊 Column Categories")
        categories = basic_info['column_categories']
        
        for category, columns in categories.items():
            if columns:
                st.write(f"**{category.replace('_', ' ').title()}** ({len(columns)} columns):")
                st.write(", ".join(columns[:10]))  # Show first 10 columns
                if len(columns) > 10:
                    st.write(f"... and {len(columns) - 10} more")
                st.write("---")
        
        # Detailed analysis
        st.subheader("📈 Detailed Analysis")
        
        # Gender analysis
        gender_analysis = analyzer.analyze_gender_distribution()
        if gender_analysis:
            st.write("**Gender Distribution:**")
            st.write(gender_analysis)
        
        # Income analysis
        income_analysis = analyzer.analyze_income_distribution()
        if income_analysis:
            st.write("**Income Analysis:**")
            for col, stats in income_analysis.items():
                st.write(f"**{col}:**")
                st.write(f"  - Mean: {stats['mean']:,.2f}")
                st.write(f"  - Median: {stats['median']:,.2f}")
                st.write(f"  - Std Dev: {stats['std']:,.2f}")
        
        # Loan amounts analysis
        loan_analysis = analyzer.analyze_loan_amounts()
        if loan_analysis:
            st.write("**Loan Amounts Analysis:**")
            for col, stats in loan_analysis.items():
                st.write(f"**{col}:**")
                st.write(f"  - Total: {stats['total']:,.2f}")
                st.write(f"  - Mean: {stats['mean']:,.2f}")
                st.write(f"  - Max: {stats['max']:,.2f}")
        
        # Geographic analysis
        geo_analysis = analyzer.analyze_geographic_distribution()
        if geo_analysis:
            st.write("**Geographic Distribution:**")
            if 'states' in geo_analysis:
                st.write(f"**States:** {geo_analysis['states']['total_states']} unique states")
                st.write("Top 5 states:")
                for state, count in list(geo_analysis['states']['top_10'].items())[:5]:
                    st.write(f"  - {state}: {count:,}")
        
        # Data preview
        st.subheader("📋 Data Preview")
        st.dataframe(analyzer.df.head(10))
        
    except Exception as e:
        st.error(f"Error analyzing data: {str(e)}")
        st.info("Please ensure the test.csv file is in the Data/raw/ directory")

def show_visualizations():
    """Display visualizations page"""
    st.header("📊 Data Visualizations")
    
    # Sample visualizations
    st.subheader("Sample Charts")
    
    # Bar chart
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [23, 45, 56, 78, 32]
    
    fig_bar = px.bar(x=categories, y=values, title="Sample Bar Chart")
    st.plotly_chart(fig_bar, use_container_width=True)
    
    # Pie chart
    fig_pie = px.pie(values=values, names=categories, title="Sample Pie Chart")
    st.plotly_chart(fig_pie, use_container_width=True)

def show_predictions():
    """Display predictions page"""
    st.header("🔮 Predictions & ML Models")
    
    st.info("This section will contain machine learning models and predictions.")
    
    # Placeholder for ML functionality
    st.write("Coming soon: Machine learning models and predictive analytics")

def show_settings():
    """Display settings page"""
    st.header("⚙️ Settings")
    
    st.subheader("Dashboard Configuration")
    
    # Theme selection
    theme = st.selectbox("Select Theme", ["Light", "Dark", "Auto"])
    
    # Refresh rate
    refresh_rate = st.slider("Auto-refresh rate (seconds)", 0, 60, 30)
    
    # Save settings
    if st.button("Save Settings"):
        st.success("Settings saved successfully!")

if __name__ == "__main__":
    import numpy as np
    main() 