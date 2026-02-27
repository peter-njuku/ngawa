#!/bin/bash

# Exit on any error
set -e

echo "Applying database migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

# Add these lines before your ENTRYPOINT/CMD
RUN mkdir -p /app/data
RUN chmod -R 777 /app/data

echo "Starting server..."
exec "$@"
