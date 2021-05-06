#!/usr/bin/env bash
PROJECT=backend

if [ "$DJANGO_CONFIGURATION" == "Development" ]
then
    echo "=> Performing database migrations in development..."
    python manage.py reset_db -c --noinput --settings=${PROJECT}.settings --configuration=Development
    python manage.py migrate --settings=${PROJECT}.settings --configuration=Development
    python manage.py loaddata --settings=${PROJECT}.settings --configuration=Development fixtures/development.json.bz2

    echo "=> Run application in development"
    gunicorn ${PROJECT}.wsgi:application -b :8000 --timeout 120 --log-file -

elif [ "$DJANGO_CONFIGURATION" == "Staging" ]
then
    echo "=> Performing database migrations in staging..."
    python manage.py reset_db -c --noinput --settings=${PROJECT}.settings --configuration=Staging
    python manage.py migrate --settings=${PROJECT}.settings --configuration=Staging
    python manage.py loaddata --settings=${PROJECT}.settings --configuration=Staging fixtures/development.json.bz2

    echo "=> Run application in staging"
    gunicorn ${PROJECT}.wsgi:application -b :8000 --timeout 120 --log-file -
elif [ "$DJANGO_CONFIGURATION" == "Production" ]
then
    echo "=> Performing database migrations in production..."
    python manage.py migrate --settings=${PROJECT}.settings --configuration=Production

    echo "=> Run application in production"
    gunicorn ${PROJECT}.wsgi:application -b :8000 --timeout 120 --log-file -
else
    echo "No enviroment defined..."
fi