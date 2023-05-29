# django-htmx

## simple django projct for testing and developing htmx components

## Installation

### clone the repo:

- git clone https://github.com/hj-winter/angondeln-htmx.git
- cd django-htmx

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
- python manage.py createsuperuser (if needed)

### load the testdata

- python manage.py runscript load_data

### run the server

- python manage.py runserver

### load the page in the brower

- localhost:8000
