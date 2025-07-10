# Project Prompts & Templates Compilation

This document compiles and improves all the prompts and requests used in this project. Use these as templates for future projects, with suggestions for one-shot, two-shot, and extended prompts.

---

## 1. Project Setup & Structure

**One-Shot Prompt:**
> Set up a production-ready data analysis project with Streamlit and Dash, including a modular source code structure, data directories, configuration, utility modules, and Docker deployment. Add unit tests, documentation, and example data integration.

**Two-Shot Prompt:**
> 1. Create a project structure for a financial data analysis dashboard using Streamlit and Dash, with separate folders for data, source code, and documentation.
> 2. Add utility modules for data loading and analysis, and set up Docker deployment scripts for all services.

**More Details to Add:**
- Specify Python version and dependency management (e.g., pip, poetry)
- Request example config files and .env templates
- Ask for sample test cases and CI/CD setup

---

## 2. Deployment & Dockerization

**One-Shot Prompt:**
> Make the project fully deployable with Docker Compose, including services for Streamlit, Dash, REST API (Flask), FastAPI, and nginx as a reverse proxy. Provide deployment scripts for Windows and Linux/Mac.

**Two-Shot Prompt:**
> 1. Add Dockerfile and docker-compose.yml for all services, with health checks and shared volumes.
> 2. Create deploy.sh and deploy.bat scripts for one-command deployment and service health verification.

**More Details to Add:**
- Request HTTPS/SSL setup and production environment variables
- Ask for cloud deployment options (AWS, Azure, GCP)
- Request monitoring/logging integration

---

## 3. Learning Resource Support

**One-Shot Prompt:**
> Create a learning resource folder with a structured .md file for each technology used (Streamlit, Dash, FastAPI, Flask, Docker, Nginx, Pandas, project structure, internal paths). Include overview, key concepts, syntax, use cases, setup, best practices, pros/cons, keywords, and external links.

**Two-Shot Prompt:**
> 1. For each major tool (Streamlit, Dash, etc.), create a markdown learning guide with glossary, code examples, and project-specific usage.
> 2. Add a summary file comparing all choices, alternatives, and future options.

**More Details to Add:**
- Request code snippets for each keyword
- Ask for cross-references between files
- Request a quickstart guide for new team members

---

## 4. Troubleshooting & Error Handling

**One-Shot Prompt:**
> If a service fails to start, diagnose the error and provide step-by-step fixes, including missing dependencies, port conflicts, and code deprecations.

**Two-Shot Prompt:**
> 1. I get a 'ModuleNotFoundError' or 'AttributeError' when launching a service. What should I do?
> 2. How can I ensure all dependencies are installed and up to date?

**More Details to Add:**
- Request a troubleshooting checklist for each service
- Ask for automated health check scripts
- Request a summary of common error messages and solutions

---

## 5. Service Launch & Automation

**One-Shot Prompt:**
> Create a main.py that lets me launch all services (Streamlit, Dash, REST API, FastAPI) from a single command, and writes all service URLs to a file for easy access.

**Two-Shot Prompt:**
> 1. Add a CLI to main.py for launching individual or all services.
> 2. Store the service URLs in a text file after launch.

**More Details to Add:**
- Request logging of process status and errors
- Ask for a web dashboard to monitor service health

---

## 6. User Experience & Documentation

**One-Shot Prompt:**
> Add a deployment guide and architecture diagram to the docs, showing how all services interact and how to deploy the project step by step.

**Two-Shot Prompt:**
> 1. Create a Mermaid diagram of the deployment architecture.
> 2. Add a section to the deployment guide explaining the flow and best practices.

**More Details to Add:**
- Request onboarding checklists for new developers
- Ask for a FAQ section in the docs

---

## 7. Advanced Prompts for Future Projects

- Request integration with authentication and user management
- Ask for cloud-native deployment (Kubernetes, serverless)
- Request automated testing and CI/CD pipelines
- Ask for performance benchmarking and optimization tips
- Request accessibility and internationalization support

---

**How to Use This File:**
- Copy and adapt these prompts for new projects
- Use the 'More Details to Add' to expand requirements
- Combine one-shot and two-shot prompts for iterative development 