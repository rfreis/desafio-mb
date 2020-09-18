#!/bin/bash

cd /app

if [ ! -f ".env" ]; then
  cp .env.example .env
fi

python manage.py migrate
python manage.py runserver 0.0.0.0:8000 > log.txt
