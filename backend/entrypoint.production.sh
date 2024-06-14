#!/bin/sh
poetry shell
poetry run wait-for
poetry run python manage.py migrate
poetry run python manage.py compilemessages
poetry run python manage.py collectstatic --noinput
exec "$@"
