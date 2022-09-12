#!/usr/bin/env sh

make migrate

python manage.py runserver 8000