# Dash Learning Resource

## Overview
Dash is a Python framework for building analytical web applications, especially suited for data visualization with Plotly.

## Key Concepts & Glossary
- **Layout**: Structure of the app (HTML components, graphs, etc.)
- **Callback**: Function that updates UI in response to user input
- **dcc.Graph**: Plotly chart component
- **dash.dependencies**: Used for callback inputs/outputs

## Syntax & Examples
```python
import dash
from dash import html, dcc
app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Input(id='input', value='world'),
    html.Div(id='output')
])
@app.callback(
    dash.dependencies.Output('output', 'children'),
    [dash.dependencies.Input('input', 'value')])
def update_output(value):
    return f'Hello {value}'
if __name__ == '__main__':
    app.run_server(debug=True)
```

## Common Use Cases
- Interactive dashboards
- Data visualization apps
- Real-time data monitoring

## Setup & Usage
```bash
pip install dash
python app.py
```

## Best Practices
- Use callbacks efficiently (avoid circular dependencies)
- Modularize code for large apps
- Use dcc.Store for client-side state

## External Learning Links
- [Dash Docs](https://dash.plotly.com/introduction)
- [Dash by Plotly YouTube](https://www.youtube.com/results?search_query=dash+plotly+tutorial)
- [Awesome Dash](https://github.com/ucg8j/awesome-dash)

## How Dash is Used in This Project
- Advanced dashboard for interactive analytics
- Real-time and multi-page visualizations
- Entry point: `src/dash/app.py` 

## Core Concepts Used in This Project
- Used for advanced, interactive analytics dashboards.
- Chosen for its flexibility, Plotly integration, and callback system.
- Used callbacks, dcc.Graph, and modular layouts.

## Ignored/Alternative Concepts
- Not used: Bokeh, Panel, Streamlit, or custom React dashboards.
- Reason: Dash offers more control and is better for complex, multi-page apps.

## Other Concepts You Could Use
- Dash Enterprise for deployment
- Integration with authentication and user management
- Use of Dash DataTable for large datasets

## Technology Foundations
- Built on Flask, React.js, and Plotly.js.

## Advantages & Disadvantages
**Advantages:**
- Highly customizable and powerful for data visualization
- Supports complex, multi-page apps
- Tight Plotly integration

**Disadvantages:**
- More boilerplate than Streamlit
- Callback logic can get complex
- Slower to prototype than Streamlit 

## Project Keywords Used (with Use & Summary)
- **dash.Dash**: Main Dash app object; initializes the dashboard server.
- **dash.html**: Provides HTML components for layout (e.g., Div, H1).
- **dash.dcc**: Provides interactive components (e.g., Graph, Input).
- **dcc.Input**: User input field for filtering/searching data.
- **dcc.Graph**: Renders Plotly charts for data visualization.
- **html.Div**: Container for grouping layout elements.
- **@app.callback**: Decorator to define reactive functions that update UI based on user input.
- **dash.dependencies.Input**: Specifies which component property triggers a callback.
- **dash.dependencies.Output**: Specifies which component property is updated by a callback.
- **Modular layouts**: Organizes the dashboard into reusable sections/pages.
- **Real-time visualizations**: Updates charts and metrics as data changes or user interacts. 