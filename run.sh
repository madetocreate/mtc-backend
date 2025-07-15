#!/bin/bash
cd "$(dirname "$0")"
source venv/bin/activate
echo "🔥 Starte FastAPI-Server auf Port 8001..."
PYTHONPATH=. uvicorn api.api:app --reload --port 8001

