#!/bin/sh

set -e

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate

gunicorn qnode0_app.wsgi:application --workers 4 --bind 0.0.0.0:8000
#uwsgi --socket :9000 --workers 10 --master --enable-threads --module qnode0_app.wsgi