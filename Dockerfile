# Base image
FROM python:3.11-slim

# Working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Django project
COPY . .

# Collect static files and apply migrations (you can override in docker-compose command too)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
