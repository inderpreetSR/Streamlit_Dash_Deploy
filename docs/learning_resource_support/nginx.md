# Nginx Learning Resource

## Overview
Nginx is a high-performance web server, reverse proxy, and load balancer, widely used for serving static content and routing traffic to backend services.

## Key Concepts & Glossary
- **Reverse Proxy**: Forwards client requests to backend servers
- **Server Block**: Configuration for a domain/port
- **Upstream**: Group of backend servers
- **Location Block**: URL path routing

## Syntax & Examples
```nginx
server {
    listen 80;
    server_name example.com;
    location /api/ {
        proxy_pass http://backend:5000/;
    }
}
```

## Common Use Cases
- Load balancing
- SSL termination
- API gateway
- Static file serving

## Setup & Usage
- [Install Nginx](https://nginx.org/en/docs/install.html)
- Start: `nginx`
- Config: `/etc/nginx/nginx.conf`

## Best Practices
- Use separate server blocks for each service
- Enable gzip compression
- Use rate limiting and security headers

## External Learning Links
- [Nginx Docs](https://nginx.org/en/docs/)
- [Nginx Beginner’s Guide](https://www.digitalocean.com/community/tutorial_series/nginx-basics)
- [Awesome Nginx](https://github.com/agile6v/awesome-nginx)

## How Nginx is Used in This Project
- Reverse proxies requests to Streamlit, Dash, REST API, and FastAPI
- Handles SSL, rate limiting, and health checks
- See `nginx.conf` 

## Core Concepts Used in This Project
- Used as a reverse proxy and load balancer for all app services.
- Chosen for performance, flexibility, and security features.
- Used server blocks, upstreams, and SSL/rate limiting.

## Ignored/Alternative Concepts
- Not used: Apache HTTPD, Caddy, Traefik, or HAProxy.
- Reason: Nginx is lightweight, fast, and widely supported in Docker.

## Other Concepts You Could Use
- Traefik for dynamic Docker routing
- Caddy for automatic HTTPS
- Nginx Plus for advanced features

## Technology Foundations
- Written in C, event-driven architecture.

## Advantages & Disadvantages
**Advantages:**
- Extremely fast and efficient
- Handles high concurrency
- Flexible configuration

**Disadvantages:**
- Config syntax can be tricky
- Less dynamic than Traefik
- Advanced features require manual config 

## Project Keywords Used
- nginx.conf
- server block
- location block
- upstream
- proxy_pass
- listen
- add_header
- gzip
- limit_req
- SSL
- Health check endpoint 