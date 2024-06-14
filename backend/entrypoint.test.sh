#!/bin/sh
poetry run
poetry run wait-for
exec "$@"
