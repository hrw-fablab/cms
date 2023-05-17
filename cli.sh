#!/bin/bash
exec >logfile.txt 2>&1
poetry install
poetry run python manage.py migrate --settings=cms.settings.production
poetry run python manage.py collectstatic --noinput
touch tmp/restart.txt
