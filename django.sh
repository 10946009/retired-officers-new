#!/bin/sh

# Collect static files
echo "Collect static files"
poetry run python manage.py collectstatic --noinput

# Start server
echo "Starting server"
poetry run python manage.py runserver 0.0.0.0:8000