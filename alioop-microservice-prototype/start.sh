#!/bin/bash
cd /workspaces/audomte/alioop-microservice-prototype
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
