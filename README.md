# django_api

we are going to use TastyPie library to set up a simple API using Django.

we will be building an API for a Google note-taking web app. We want to build a REST-ful API with CRUD endpoints, to createm read, update, and delete notes.


## Setup 


### Install Django

```
pip install Django
django-admin startproject notable_django
cd notable_django
```

### Install TastyPie

```
pip install django-tastypie
```

### Start our app within our project

```
python manage.py startapp api
```
(incase of linux systems)
```
python3 manage.py startapp api
```

You may see two subfolders named `notable_django`, `api` and a `manage.py` file under 'notable_django` directory. To summarise,

- notable_django : settings for configuration of projects, usage of URLS
- api :handles actual API magic


### Install app within our project

Go inside notable_django/settings.py

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api'
]
```

Here, our project is `notable_django` and app is `api` . Other apps may or may not be useful.