import argparse
import subprocess
import sys
import os

SERVICES = {
    'streamlit': ['streamlit', 'run', 'src/streamlit/app.py'],
    'dash': [sys.executable, 'src/dash/app.py'],
    'restapi': [sys.executable, 'src/api/rest_api.py'],
    'fastapi': ['uvicorn', 'src.api.fast_api:app', '--reload'],
}

SERVICE_LINKS = [
    "Streamlit: http://localhost:8501",
    "Dash: http://localhost:8050",
    "REST API: http://localhost:5000",
    "FastAPI: http://localhost:8000",
    "FastAPI Docs: http://localhost:8000/docs"
]

def run_service(name):
    print(f"\nLaunching {name}...")
    try:
        subprocess.Popen(SERVICES[name])
        print(f"{name.capitalize()} started. See its local port.")
    except Exception as e:
        print(f"Failed to start {name}: {e}")

def write_service_links():
    with open("service_links.txt", "w") as f:
        f.write("Project Service Links\n====================\n")
        for link in SERVICE_LINKS:
            f.write(link + "\n")

def main():
    parser = argparse.ArgumentParser(description="Launch project services.")
    parser.add_argument('--all', action='store_true', help='Start all services')
    parser.add_argument('--streamlit', action='store_true', help='Start Streamlit app')
    parser.add_argument('--dash', action='store_true', help='Start Dash app')
    parser.add_argument('--restapi', action='store_true', help='Start REST API (Flask)')
    parser.add_argument('--fastapi', action='store_true', help='Start FastAPI app')
    args = parser.parse_args()

    if args.all or not any(vars(args).values()):
        print("Starting all services (Streamlit, Dash, REST API, FastAPI)...")
        for name in SERVICES:
            run_service(name)
        print("\nAll services launched. Access them at:")
        for link in SERVICE_LINKS:
            print(f"  {link}")
        write_service_links()
    else:
        for name in SERVICES:
            if getattr(args, name):
                run_service(name)
        # Optionally write links if any service is started
        write_service_links()

if __name__ == '__main__':
    main() 