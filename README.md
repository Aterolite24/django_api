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


## Note Model

Let's 1st understand models with following analogy. Imagine u have a toy box and in toy box you have different toys like : cars, dolls and blocks.

Now think Django as toy box where you keep information instead of toys. In Django we use `models` to describe different types of information. Just like labels for toys.

- **Model** : it is like description/features of one type of toy. ex : for car, it might be no. of wheels, colour, etc.

- **Fields** : fields are those specific features of toys. It holds data for each feature. ex : for car,
    - wheel : 4
    - colour : red
    - size : small

- **Database** : This is like toy box itself. Whenever you buy a new toy you put it in toy box. Similarly, whenever you create a new object, its information gets store in database.


### Create our Model

Each model is a python class that subclasses `django.db.models.Model` . Each attribute of model represents a database field. Let `title`, `body`, and `created_at` be attributes of our note.

Going with our analogy, let's create a model for a toy car:

```
from django.db import models

class toycar(models.Model):
    color = models.CharField(max_length = 20)
    wheels = models.IntegerField()
    size = models.CharField(max_length=10)
```
`models.CharField` and `models.IntegerField` are ways to tell Django what type of data each field will hold (like words or numbers).

Now we go to api/models.py and create our model :

```
from django.db import models

class note(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
```

### adding __str__ method

When you define the `__str__` method in a Django model, you're telling Django how you want instances of that model to be represented as strings. 

Like when you create a `ToyCar` object and print it or look at it in the admin interface, you'll see something like "Red Toy Car with 4 wheels" instead of just seeing an object identifier like `ToyCar object (1)`.

```
from django.db import models

class ToyCar(models.Model):
    color = models.CharField(max_length=20)
    wheels = models.IntegerField()
    size = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.color} Toy Car with {self.wheels} wheels"
```

Similarly we do it for our Note app, we will return `title` by `__str__` method to keep things clean.

```
from django.db import models

class note(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
```


## Note Migrations

Continuing with our previous analogy, let's say you want to make changes to the toys in your toy box over time. For example, you might want to add a new type of toy, remove an old one, or change the features of an existing toy. Migrations in Django help you keep track of these changes and apply them to your toy box in an organized way.

### initial migration

Creating a note model with title, body and date created. To set this up we run following commands :

```
python3 manage.py makemigrations
python3 manage.py migrate
```

### making changes

Add the field that you want to add like `type`, important note, very important note, etc

```
# generates new migration files in Django application with changes/updates
python3 manage.py makemigrations
```

## applying new migration

You then apply these new instructions to your toy box (database) to update the existing toy cars with the new `type` feature.

```
# updating database with latest features
python manage.py migrate
```