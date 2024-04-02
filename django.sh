#!/bin/sh

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Start server
echo "Starting server"
exec python manage.py runserver 0.0.0.0:8000