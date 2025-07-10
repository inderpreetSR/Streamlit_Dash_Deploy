"""
Dash Insights Dashboard
Main application file for the Dash dashboard
"""

import dash
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Initialize the Dash app
app = dash.Dash(__name__, 
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                suppress_callback_exceptions=True)

# App layout
app.layout = html.Div([
    # Header
    html.Div([
        html.H1("📊 Data Insights Dashboard", 
                className="text-center text-primary mb-4",
                style={'fontSize': '2.5rem', 'marginTop': '20px'}),
        html.Hr()
    ]),
    
    # Navigation tabs
    dcc.Tabs([
        dcc.Tab(label='Overview', children=[
            html.Div([
                # Metrics row
                html.Div([
                    html.Div([
                        html.H4("1,234", className="text-center text-primary"),
                        html.P("Total Records", className="text-center text-muted")
                    ], className="col-md-3"),
                    html.Div([
                        html.H4("567", className="text-center text-success"),
                        html.P("Active Users", className="text-center text-muted")
                    ], className="col-md-3"),
                    html.Div([
                        html.H4("$45,678", className="text-center text-info"),
                        html.P("Revenue", className="text-center text-muted")
                    ], className="col-md-3"),
                    html.Div([
                        html.H4("3.2%", className="text-center text-warning"),
                        html.P("Conversion Rate", className="text-center text-muted")
                    ], className="col-md-3")
                ], className="row mb-4"),
                
                # Charts row
                html.Div([
                    html.Div([
                        dcc.Graph(id='time-series-chart')
                    ], className="col-md-8"),
                    html.Div([
                        dcc.Graph(id='pie-chart')
                    ], className="col-md-4")
                ], className="row")
            ], className="container-fluid")
        ]),
        
        dcc.Tab(label='Data Analysis', children=[
            html.Div([
                html.H3("🔍 Data Analysis", className="mb-3"),
                html.P("Upload your data file for analysis"),
                dcc.Upload(
                    id='upload-data',
                    children=html.Div([
                        'Drag and Drop or ',
                        html.A('Select Files')
                    ]),
                    style={
                        'width': '100%',
                        'height': '60px',
                        'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'margin': '10px'
                    },
                    multiple=False
                ),
                html.Div(id='output-data-upload')
            ], className="container-fluid")
        ]),
        
        dcc.Tab(label='Visualizations', children=[
            html.Div([
                html.H3("📊 Data Visualizations", className="mb-3"),
                html.Div([
                    html.Div([
                        dcc.Graph(id='bar-chart')
                    ], className="col-md-6"),
                    html.Div([
                        dcc.Graph(id='scatter-chart')
                    ], className="col-md-6")
                ], className="row")
            ], className="container-fluid")
        ]),
        
        dcc.Tab(label='Predictions', children=[
            html.Div([
                html.H3("🔮 Predictions & ML Models", className="mb-3"),
                dbc.Alert([
                    html.H4("Coming Soon!", className="alert-heading"),
                    html.P("Machine learning models and predictive analytics will be available here.")
                ], color="info")
            ], className="container-fluid")
        ]),
        
        dcc.Tab(label='Settings', children=[
            html.Div([
                html.H3("⚙️ Settings", className="mb-3"),
                html.Div([
                    html.Label("Theme Selection:"),
                    dcc.Dropdown(
                        id='theme-dropdown',
                        options=[
                            {'label': 'Light', 'value': 'light'},
                            {'label': 'Dark', 'value': 'dark'},
                            {'label': 'Auto', 'value': 'auto'}
                        ],
                        value='light'
                    ),
                    html.Br(),
                    html.Label("Refresh Rate (seconds):"),
                    dcc.Slider(
                        id='refresh-slider',
                        min=0,
                        max=60,
                        step=5,
                        value=30,
                        marks={i: str(i) for i in range(0, 61, 10)}
                    ),
                    html.Br(),
                    html.Button("Save Settings", id='save-settings', className="btn btn-primary")
                ])
            ], className="container-fluid")
        ])
    ])
])

# Callback for time series chart
@app.callback(
    Output('time-series-chart', 'figure'),
    Input('time-series-chart', 'id')
)
def update_time_series_chart(id):
    # Generate sample time series data
    dates = pd.date_range('2024-01-01', periods=30, freq='D')
    values = [100 + i * 2 + np.random.randint(-10, 10) for i in range(30)]
    
    df = pd.DataFrame({
        'Date': dates,
        'Value': values
    })
    
    fig = px.line(df, x='Date', y='Value', title='Sample Time Series Data')
    fig.update_layout(height=400)
    return fig

# Callback for pie chart
@app.callback(
    Output('pie-chart', 'figure'),
    Input('pie-chart', 'id')
)
def update_pie_chart(id):
    categories = ['Category A', 'Category B', 'Category C', 'Category D']
    values = [23, 45, 56, 78]
    
    fig = px.pie(values=values, names=categories, title='Sample Distribution')
    fig.update_layout(height=400)
    return fig

# Callback for bar chart
@app.callback(
    Output('bar-chart', 'figure'),
    Input('bar-chart', 'id')
)
def update_bar_chart(id):
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [23, 45, 56, 78, 32]
    
    fig = px.bar(x=categories, y=values, title='Sample Bar Chart')
    fig.update_layout(height=400)
    return fig

# Callback for scatter chart
@app.callback(
    Output('scatter-chart', 'figure'),
    Input('scatter-chart', 'id')
)
def update_scatter_chart(id):
    # Generate sample scatter data
    np.random.seed(42)
    x = np.random.randn(100)
    y = 2 * x + np.random.randn(100)
    
    fig = px.scatter(x=x, y=y, title='Sample Scatter Plot')
    fig.update_layout(height=400)
    return fig

# Callback for file upload
@app.callback(
    Output('output-data-upload', 'children'),
    Input('upload-data', 'contents'),
    Input('upload-data', 'filename')
)
def update_output(contents, filename):
    if contents is not None:
        # Parse uploaded file
        import base64
        import io
        
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        
        try:
            if 'csv' in filename:
                df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
            elif 'xls' in filename:
                df = pd.read_excel(io.BytesIO(decoded))
            else:
                return html.Div(['Please upload a CSV or Excel file.'])
            
            return html.Div([
                html.H5(f'File: {filename}'),
                html.H6(f'Shape: {df.shape}'),
                html.Div([
                    html.H6('Data Preview:'),
                    dash.dash_table.DataTable(
                        data=df.head().to_dict('records'),
                        columns=[{'name': i, 'id': i} for i in df.columns],
                        page_size=5
                    )
                ])
            ])
        except Exception as e:
            return html.Div(['Error processing this file.'])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050) 