# Docker Learning Resource

## Overview
Docker is a platform for developing, shipping, and running applications in containers—lightweight, portable, and consistent environments.

## Key Concepts & Glossary
- **Image**: Blueprint for a container
- **Container**: Running instance of an image
- **Dockerfile**: Script to build images
- **Volume**: Persistent storage
- **Network**: Communication between containers
- **docker-compose**: Tool for multi-container orchestration

## Syntax & Examples
```bash
# Build image
docker build -t myapp .
# Run container
docker run -p 8501:8501 myapp
# Compose up
docker-compose up -d
```

## Common Use Cases
- Isolated dev environments
- Microservices deployment
- CI/CD pipelines

## Setup & Usage
- [Install Docker](https://docs.docker.com/get-docker/)
- [Install Docker Compose](https://docs.docker.com/compose/install/)

## Best Practices
- Use .dockerignore to reduce image size
- Keep images minimal (use slim base images)
- Use named volumes for persistent data

## External Learning Links
- [Docker Docs](https://docs.docker.com/)
- [Docker Getting Started](https://docs.docker.com/get-started/)
- [Awesome Docker](https://github.com/veggiemonk/awesome-docker)

## How Docker is Used in This Project
- Containerizes all services (Streamlit, Dash, APIs)
- Orchestrates with docker-compose
- See `Dockerfile` and `docker-compose.yml` 

## Core Concepts Used in This Project
- Used for containerizing all services and orchestrating with docker-compose.
- Chosen for reproducibility, portability, and ease of deployment.
- Used Dockerfile, volumes, and custom entrypoints.

## Ignored/Alternative Concepts
- Not used: Podman, Vagrant, direct VM deployment, or Kubernetes (for this scale).
- Reason: Docker is the industry standard for small-to-medium projects.

## Other Concepts You Could Use
- Kubernetes for large-scale orchestration
- Docker Swarm for clustering
- BuildKit for advanced builds

## Technology Foundations
- Built on Linux container technology (namespaces, cgroups).

## Advantages & Disadvantages
**Advantages:**
- Consistent environments across dev and prod
- Easy to share and deploy
- Large ecosystem and tooling

**Disadvantages:**
- Adds complexity for small/simple projects
- Requires learning Docker concepts
- Not a full VM (some isolation limits) 

## Project Keywords Used
- Dockerfile
- docker-compose.yml
- docker build
- docker run
- docker-compose up
- docker-compose down
- Volumes
- Networks
- EXPOSE
- ENTRYPOINT
- Healthcheck 