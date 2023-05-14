#!/bin/bash
poetry run python manage.py migrate --settings=settings.production
poetry run python manage.py collectstatic --noinput
touch tmp/restart.txt