## About this project

This is a toy project created by SambaGod to practice his Django skills and to learn new backend trends and technologies.
This code was assisted by freecodecamp.org

## Seting up the environment

- Install Django: `python3 -m pip install Django`
- Create Project: `django-admin startproject django_toy`
- Create an app/module: `python3 manage.py startapp meetups`
  All installed apps must be connected to the root project inside settings.py -> installed apps
- Run development server: `python3 manage.py runserver`
- Turn model into migration: `python3 manage.py makemigrations`
- Run migrations: `python3 manage.py migrate`
- Create User: `python3 manage.py createsuperuser`
- Install Pillow for image handling `python3 -m pip install Pillow`

## Name conventions

Name conventions in Django are important for example directories like templates, migrations, static etc. should be named exactly that way
