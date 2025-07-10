# Streamlit Learning Resource

## Overview
Streamlit is an open-source Python library for building interactive web apps for data science and machine learning projects with minimal effort.

## Key Concepts & Glossary
- **Widget**: UI element (slider, button, etc.) for user interaction.
- **st.write()**: Universal function to display text, data, charts, etc.
- **st.sidebar**: Place widgets in a sidebar.
- **st.dataframe()**: Display a pandas DataFrame interactively.
- **Session State**: Store variables across interactions.

## Syntax & Examples
```python
import streamlit as st
st.title('My App')
name = st.text_input('Enter your name:')
st.write(f'Hello, {name}!')
```

## Common Use Cases
- Data dashboards
- ML model demos
- Interactive data exploration
- Real-time visualizations

## Setup & Usage
```bash
pip install streamlit
streamlit run app.py
```

## Best Practices
- Use caching (`@st.cache_data`) for expensive computations
- Keep UI simple and responsive
- Use session state for multi-step workflows

## External Learning Links
- [Streamlit Docs](https://docs.streamlit.io/)
- [Streamlit Tutorials (YouTube)](https://www.youtube.com/results?search_query=streamlit+tutorial)
- [Awesome Streamlit](https://github.com/MarcSkovMadsen/awesome-streamlit)

## How Streamlit is Used in This Project
- Main dashboard for data analysis and visualization
- Multi-page navigation, real-time metrics, and interactive widgets
- Entry point: `src/streamlit/app.py` 

## Core Concepts Used in This Project
- Used for rapid, interactive dashboard development.
- Chosen for its simplicity, fast prototyping, and Python-native syntax.
- Used widgets, session state, and caching for user interaction and performance.

## Ignored/Alternative Concepts
- Not used: Shiny (R), Voila, Panel, Gradio, or custom Flask/React dashboards.
- Reason: Streamlit is more Pythonic, easier for data science, and has a lower learning curve.

## Other Concepts You Could Use
- Streamlit Components (custom JS widgets)
- Integration with authentication (e.g., Streamlit-Auth0)
- Deployment on Streamlit Cloud or Heroku

## Technology Foundations
- Built on Tornado web server, Python, and WebSockets for real-time updates.

## Advantages & Disadvantages
**Advantages:**
- Very fast to build and deploy
- Minimal code for interactive UIs
- Great for data science and ML demos

**Disadvantages:**
- Limited customization compared to full-stack frameworks
- Not ideal for complex, multi-user apps
- Fewer advanced UI components than Dash or React 

## Project Keywords Used (with Use & Summary)
- **st.write**: Displays text, data, and visualizations; used for all output in the dashboard.
- **st.title**: Sets the main title of the app page.
- **st.text_input**: Collects user input for filtering or searching data.
- **st.dataframe**: Shows pandas DataFrames interactively for data exploration.
- **st.sidebar**: Places filters and navigation in a sidebar for better UX.
- **st.cache_data**: Caches expensive computations to speed up repeated operations.
- **st.session_state**: Stores variables across user interactions (e.g., multi-step workflows).
- **streamlit run**: CLI command to launch the Streamlit app.
- **Multi-page navigation**: Allows users to switch between different dashboard pages.
- **Real-time metrics**: Displays live-updating statistics and KPIs.
- **Interactive widgets**: Sliders, buttons, and other UI elements for user interaction. 