#!/bin/bash

# Exit on any error
set -e

# Ensure the data directory exists and is writable
mkdir -p /app/data
chmod 777 /app/data

echo "Applying database migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting server..."

# Use PORT environment variable if set (for Render), default to 8000
PORT=${PORT:-8000}

# If we're on Render, run Gunicorn
if [ -n "${RENDER}" ]; then
    echo "Running on Render on port $PORT"
    exec gunicorn ngawa.wsgi:application --bind 0.0.0.0:$PORT --workers 3
else
    # For Docker Compose or local development
    exec "$@"
fi
