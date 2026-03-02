#!/bin/bash
set -e

echo "Running database migrations..."
alembic upgrade head

echo "Seeding initial data..."
python seed_chart_accounts.py

echo "Starting Bridge API..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
