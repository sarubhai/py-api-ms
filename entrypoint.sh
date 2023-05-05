#!/bin/sh

echo "Waiting for PostgreSQL..."

while ! nc -z $POSTGRES_HOSTNAME $POSTGRES_PORT; do
  sleep 0.1
done

echo "PostgreSQL Started"

gunicorn -b 0.0.0.0:$APP_PORT manage:app --timeout 120 --workers=3 --threads=3 --worker-connections=1000