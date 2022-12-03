# Django Dash Demo
based on https://docs.djangoproject.com/en/4.1/intro/tutorial01/

### Build Django Project 

- build python env in pycharm
- python -m pip install Django
- django-admin startproject demo_site
- ./manage.py migrate
- ./manage.py runserver

### Adds Django app & templates

- ./manage.py startapp zdemo
- create the templates folder and add it to the templates settings.
- create and link a new view in zdemo/views - the view would return 
template file exists under the /templates.