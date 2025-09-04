#!/bin/sh
source .venv/bin/activate
python manage.py runserver 0.0.0.0:$PORT