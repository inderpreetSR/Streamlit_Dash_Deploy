# Project Concepts and Choices

This document summarizes the major technologies, concepts, and design decisions for this project, including what was chosen, what was not, and why.

| Technology/Concept | Used? | Why Chosen | Alternatives Not Used | Why Not Used | Future Options |
|--------------------|-------|------------|----------------------|--------------|---------------|
| Streamlit         | Yes   | Fast prototyping, easy Python dashboards | Voila, Panel, Gradio, Shiny | Less Pythonic, less community support | Streamlit Components, Auth integration |
| Dash              | Yes   | Advanced, customizable dashboards | Bokeh, Panel, React | Less flexible, more complex | Dash Enterprise, DataTable |
| FastAPI           | Yes   | Async, fast, auto-docs | Flask-RESTful, Django REST, Falcon | Less modern, less async | WebSockets, OAuth2 |
| Flask             | Yes   | Simple, mature REST API | FastAPI, Django REST, Falcon | Less familiar, more setup | Flask-RESTful, JWT |
| Pandas            | Yes   | Flexible, powerful data analysis | Dask, Polars, SQL | Not needed for in-memory | Dask, Polars |
| Docker            | Yes   | Reproducible, portable deployment | Podman, Vagrant, Kubernetes | Overkill for small scale | Kubernetes |
| Nginx             | Yes   | Fast, flexible reverse proxy | Apache, Traefik, Caddy | Heavier, less Docker-friendly | Traefik, Caddy |
| Modular Structure | Yes   | Maintainable, scalable | Monolithic, flat | Not scalable | Monorepo, CI/CD |
| os/pathlib/config | Yes   | Robust, cross-platform paths | Hardcoded, sys.path hacks | Error-prone | pydantic-settings |

## Notes
- Choices were made for simplicity, maintainability, and best fit for a data science/web stack.
- Alternatives were not used if they were more complex, less Pythonic, or not needed for project scale.
- Future options include scaling to Kubernetes, adding authentication, or using more advanced config management. 