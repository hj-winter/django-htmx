#! /bin/bash

rm */migrations/00*
rm db.sqlite3
python manage.py makemigrations
python manage.py migrate
python manage.py runscript load_data
python manage.py runscript load_article_data