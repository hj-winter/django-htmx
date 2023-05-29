# django-htmx

## simple django projct for testing and developing htmx components

## Installation

## create directory for the project i.e. "django-htmx"

## clone the repo:

- https://github.com/hj-winter/django-htmx.git

### create virtual environment

- python3 -m venv env
- source env/bin/activate

### update pip package manager

- pip install -U pip

### install packages

- pip install -r requirements.txt

### migrate the database

- python manage.py makemigrations
- python manage.py migrate
- python manage.py createseupruser (if needed)

### load the testdata

- python manage.py runscript load_data

### run the server

- python manage.py runserver
