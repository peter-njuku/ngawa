# Python web application container
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy project source
COPY . /app/

# Collect static files (if any)
RUN python manage.py collectstatic --noinput

# Expose port for gunicorn
EXPOSE 8000

# Default command
CMD ["gunicorn", "ngawa.wsgi:application", "--bind", "0.0.0.0:8000"]
