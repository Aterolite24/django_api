# Django_api_using_TastyPie

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

> Remember ! In Python, class names typically use CamelCase.

```
from django.db import models

class ToyCar(models.Model):
    color = models.CharField(max_length = 20)
    wheels = models.IntegerField()
    size = models.CharField(max_length=10)
```
`models.CharField` and `models.IntegerField` are ways to tell Django what type of data each field will hold (like words or numbers).

Now we go to api/models.py and create our model :

```
from django.db import models

class Note(models.Model):
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

class Note(models.Model):
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

### applying new migration

You then apply these new instructions to your toy box (database) to update the existing toy cars with the new `type` feature.

```
# updating database with latest features
python manage.py migrate
```

### testing / adding note to our database

Now let's add a single note to our database to make sure our code so far works smoothly. We first create a note, save it and then call for all notes in database.

```
python3 manage.py shell
>>> from api.models import Note
>>> note = Note(title="First note", body="Congratulations! U made ur 1st note")
>>> note.save()
>>> Note.objects.all()
<QuerySet [<note: First Note>]>
>>> exit()
```


## API-fication

### Endpoints

Endpoints are like "stations" where kids can perform certain actions, like viewing the toys, adding new toys, updating toys, or removing toys. These endpoints define where the resources can be accessed or manipulated using standard HTTP methods :

    - **View All notes** : `GET /api/notes/`

    - **View a specific note** : `GET /api/notes/<id>/`

    - **Add a new note** : `POST /api/notes/<id>/`

    - **Update a note** : `PUT /api/notes/<id>/`

    - **Remove a note** : `DELETE /api/notes/<id>/`

One of the basics of `RESTful APIs` is the idea of `resources`. The term is rather abstract, but in this context it refers to a class that sits between our URLs and our models.

A user will make a request to an endpoint. Depending on the URL, the user will be redirected to a particular resource, which will then perform the appropriate `CRUD`(creating, reading, updating, deleting) action on the model/database.


### creating resources

When we create a resource in Tastypie, it's like labeling specific toys (data models) in the toy box so that children (users) can find and play with them. We import our model, create a resource from it. 

- **Resource Definition** : You define a resource called NoteResource that corresponds to the `note` model.
- **QuerySet** : specifies the set of Note objects that this resource will operate on, instances of the note model `note.objects.all()`.
- **Resource Name** : The resource is named `note1`, which determines the endpoint URL for this resource.

> Remember ! The Meta class inside noteResource should start with an uppercase 'M'

```
from api.models import Note
from tastypie.resources import ModelResource

class NoteResource(ModelResource):
    class Meta:
        queryset = note.objects.all()
        resource_name = 'note'
```

### redirecting to resources

Just like listing toys in the toy box menu, we need to configure URLs so that children (users) can find and access the toys using the labels. So we go to notable_django/urls.py :

```
from django.contrib import admin
from django.urls import re_path, include
from api.resources import NoteResource

note_resource = NoteResource()

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api/', include(note_resource.urls))
]
```


### testing our API

We’re going to use [Postman](https://www.postman.com/) to make API requests. It is a popular API development tool that allows developers to create, test, and manage API requests.

```
# to runserver
python3 manage.py runserver
```
