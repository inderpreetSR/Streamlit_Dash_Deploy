#!/bin/bash

# Streamlit & Dash Insights Project - Deployment Script
# This script sets up and deploys the complete application stack

set -e  # Exit on any error

echo "🚀 Starting Streamlit & Dash Insights Project Deployment..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if Docker is installed
check_docker() {
    print_status "Checking Docker installation..."
    if ! command -v docker &> /dev/null; then
        print_error "Docker is not installed. Please install Docker first."
        exit 1
    fi
    
    if ! command -v docker-compose &> /dev/null; then
        print_error "Docker Compose is not installed. Please install Docker Compose first."
        exit 1
    fi
    
    print_success "Docker and Docker Compose are installed"
}

# Check if data file exists
check_data() {
    print_status "Checking data file..."
    if [ ! -f "Data/raw/test.csv" ]; then
        print_warning "Data file not found at Data/raw/test.csv"
        print_status "Please ensure your data file is placed in Data/raw/test.csv"
        read -p "Do you want to continue without data? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            print_error "Deployment cancelled"
            exit 1
        fi
    else
        print_success "Data file found"
    fi
}

# Build and start services
deploy_services() {
    print_status "Building and starting services..."
    
    # Stop any existing containers
    docker-compose down --remove-orphans
    
    # Build images
    print_status "Building Docker images..."
    docker-compose build --no-cache
    
    # Start services
    print_status "Starting services..."
    docker-compose up -d
    
    print_success "Services started successfully"
}

# Wait for services to be ready
wait_for_services() {
    print_status "Waiting for services to be ready..."
    
    # Wait for Streamlit
    print_status "Waiting for Streamlit..."
    timeout=60
    while ! curl -s http://localhost:8501 > /dev/null; do
        if [ $timeout -le 0 ]; then
            print_error "Timeout waiting for Streamlit"
            break
        fi
        sleep 2
        timeout=$((timeout - 2))
    done
    
    # Wait for Dash
    print_status "Waiting for Dash..."
    timeout=60
    while ! curl -s http://localhost:8050 > /dev/null; do
        if [ $timeout -le 0 ]; then
            print_error "Timeout waiting for Dash"
            break
        fi
        sleep 2
        timeout=$((timeout - 2))
    done
    
    # Wait for REST API
    print_status "Waiting for REST API..."
    timeout=60
    while ! curl -s http://localhost:5000 > /dev/null; do
        if [ $timeout -le 0 ]; then
            print_error "Timeout waiting for REST API"
            break
        fi
        sleep 2
        timeout=$((timeout - 2))
    done
    
    # Wait for FastAPI
    print_status "Waiting for FastAPI..."
    timeout=60
    while ! curl -s http://localhost:8000 > /dev/null; do
        if [ $timeout -le 0 ]; then
            print_error "Timeout waiting for FastAPI"
            break
        fi
        sleep 2
        timeout=$((timeout - 2))
    done
    
    print_success "All services are ready"
}

# Display service information
show_services() {
    echo
    print_success "🎉 Deployment Complete!"
    echo
    echo "📊 Available Services:"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "🌐 Streamlit Dashboard:  http://localhost:8501"
    echo "📈 Dash Dashboard:       http://localhost:8050"
    echo "🔗 REST API:            http://localhost:5000"
    echo "⚡ FastAPI:             http://localhost:8000"
    echo "📚 FastAPI Docs:        http://localhost:8000/docs"
    echo "📖 FastAPI ReDoc:       http://localhost:8000/redoc"
    echo
    echo "🔧 Management Commands:"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "View logs:              docker-compose logs -f"
    echo "Stop services:          docker-compose down"
    echo "Restart services:       docker-compose restart"
    echo "Update services:        docker-compose pull && docker-compose up -d"
    echo
    echo "📋 API Endpoints:"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "REST API Health:        http://localhost:5000/api/health"
    echo "FastAPI Health:         http://localhost:8000/health"
    echo "Data Info:              http://localhost:5000/api/data/info"
    echo "Sample Data:            http://localhost:5000/api/data/sample"
    echo "Gender Analysis:        http://localhost:5000/api/analysis/gender"
    echo "Income Analysis:        http://localhost:5000/api/analysis/income"
    echo "Loan Analysis:          http://localhost:5000/api/analysis/loan"
    echo
}

# Check service health
check_health() {
    print_status "Checking service health..."
    
    services=(
        "http://localhost:8501"
        "http://localhost:8050"
        "http://localhost:5000"
        "http://localhost:8000"
    )
    
    for service in "${services[@]}"; do
        if curl -s "$service" > /dev/null; then
            print_success "$service is healthy"
        else
            print_warning "$service is not responding"
        fi
    done
}

# Main deployment function
main() {
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "🚀 Streamlit & Dash Insights Project Deployment"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo
    
    check_docker
    check_data
    deploy_services
    wait_for_services
    check_health
    show_services
    
    print_success "Deployment completed successfully!"
}

# Handle script arguments
case "${1:-}" in
    "stop")
        print_status "Stopping services..."
        docker-compose down
        print_success "Services stopped"
        ;;
    "restart")
        print_status "Restarting services..."
        docker-compose restart
        print_success "Services restarted"
        ;;
    "logs")
        print_status "Showing logs..."
        docker-compose logs -f
        ;;
    "health")
        check_health
        ;;
    "help"|"-h"|"--help")
        echo "Usage: $0 [command]"
        echo
        echo "Commands:"
        echo "  (no args)  Deploy all services"
        echo "  stop       Stop all services"
        echo "  restart    Restart all services"
        echo "  logs       Show service logs"
        echo "  health     Check service health"
        echo "  help       Show this help message"
        ;;
    *)
        main
        ;;
esac 