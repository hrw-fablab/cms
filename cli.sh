#!/bin/bash
exec >logfile.txt 2>&1
~/.local/bin/poetry install
~/.local/bin/poetry run python manage.py migrate --settings=cms.settings.production
~/.local/bin/poetry run python manage.py collectstatic --noinput
touch tmp/restart.txt
