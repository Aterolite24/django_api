# django_api

we are going to use TastyPie library to set up a simple API using Django.

we will be building an API for a Google note-taking web app. We want to build a REST-ful API with CRUD endpoints, to createm read, update, and delete notes.

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