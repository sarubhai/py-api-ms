#!/bin/sh

echo "Waiting for PostgreSQL..."

while ! nc -z $POSTGRES_HOSTNAME $POSTGRES_PORT; do
  sleep 0.1
done

echo "PostgreSQL Started"
echo $FLASK_ENV
if [ $FLASK_ENV="Development" ]
then
  python manage.py run -h 0.0.0.0
else
  gunicorn --bind 0.0.0.0:$APP_PORT manage:app --timeout 120 --workers=3 --threads=3 --worker-connections=1000
fi
