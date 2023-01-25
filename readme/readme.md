# Exchange Rates (part 1)

-------

## Problem Description

**Display exchange rates from database. Django Project.**

---

### Creating a Project

* First, we begin by installing Django by executing the command below:

```
>pip install Django
```

* Starting the project.

```
>Django-admin startproject mysite
```

* The folder structure should be as shown below:

```
|---mysite
|  |--- __init__.py
|  |--- asgi.py
|  |--- settings.py
|  |--- urls.py
|  |--- wsgi.py
|---manage.py

```

* Creating the rates app.

```
>python manage.py startapp rates
```

* The folder organization of the new application will be shown below:

```
|---rates
|  |--- migrations
|  |--- templates
|  |--- __init__.py
|  |--- admin.py
|  |--- apps.py
|  |--- models.py
|  |--- tests.py
|  |--- urls.py
|  |--- views.py

```

* In the settings.py file,we must register the created application under the installed apps as shown below:

```
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rates.apps.RatesConfig',
]
```

* Run Server.

```
>python manage.py runserver
```

---

## Database Design

(This project uses sqlite)

* We have two tables:
    * First has the following fields: **Bank**.
  ```
    bank_name,
    country,
    head_office_city,
    head_office_address,
    head_office_phone,
    email,
    website,
    usd_buy,
    usd_sell,
    eur_buy,
    eur_sell,
    rub_buy,
    rub_sell
  ```
    * Second has the following fields: **BankBranches**.
  ```
    branch_number,
    city,
    address,
    phone,
    bank_id
   ```
* The bank_id field of second table has **FOREIGN KEY** of the bank_id of the first table.

---

## Creating classes in models.py

* First, we write the classes in models.py
    * classes inherit from models.Model

```python
from django.db import models


class Bank(models.Model):
    bank_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    head_office_city = models.CharField(max_length=100)
    head_office_address = models.CharField(max_length=100)
    head_office_phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=255)
    usd_buy = models.DecimalField(max_digits=10, decimal_places=2)
    usd_sell = models.DecimalField(max_digits=10, decimal_places=2)
    eur_buy = models.DecimalField(max_digits=10, decimal_places=2)
    eur_sell = models.DecimalField(max_digits=10, decimal_places=2)
    rub_buy = models.DecimalField(max_digits=5, decimal_places=2)
    rub_sell = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.bank_name


class BankBranches(models.Model):
    branch_number = models.IntegerField(null=True)
    city = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=50, null=True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.address

```

---

## Migrations

* We write migration instructions in the terminal.

```
>pip install pillow
```

* With this command, we can see in the terminal what changes have occurred in the models.py

```
>python manage.py makemigrations
```

* With this command, we migrated and included the changes made by models.py in our project.

```
>python manage.py migrate
```

---

## Object Relational Mapping

* First, we open the shell.

```
>python manage.py shell
```

* There we import the classes of the rates module.

```
>from rates.modules import *
```

* Then we create the objects with ORM queries.
* We have created an object of the Bank class using the constructor with parameters.

```
>Bank(bank_name='Acba bank')
>b=_
>b.save()
```

* by doing save(), the information is filed in the appropriate fields of the table.

---

## Templates

* In the rates module, we create a directory called templates and create html files there.
* In the rates module, we also create a static directory, in which be located css, JavaScript and img files.
    * From the Django documentation we sweep: (for static directory)
  ```
  STATICFILES_DIRS = [
    BASE_DIR / "static"
  ]
  ```

* We create index.html file in the templates directory.
    * It consists of header and html table in which displayed exchange rates.
* There is a css file attached to index.html

---

## Controller

* For a web framework, this means handling requests and responses, setting up database connections and loading add-ons.
* We import the function of models.py into the views.py of the rates module.
* Then we import the HttpResponse from django.http
* Then we write a function that receives the request parameter.

```python
from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    bank = Bank.objects.all()
    context = {
        'bank': bank,
        'title': 'Rates.am',
    }

    return render(request, template_name='ratesPages/index.html', context=context)
```

* We assign bank variable to the Bank.objects.all() ORM method.
* In the context dictionary, we give the bank variable as a value to the 'bank' key, and we give the 'Rates.am' value to
  the 'title' key.
* Then we return render(request, template_name='ratesPages/index.html', context=context), where the template_name is
  index.html, and the context is the context dictionary.

---

## Routing

* To create route in Django, we will use the path() function that accepts two parameters: a URL and a view function.
* We create the urls.py file in the rates module.
* Then in the main urls.py we give a path to that file so that we can manage all the paths of the rates module.
    * In the main urls.py file, we import include
  ```
     from django.urls import path,include
   ```

   ```
     urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rates.urls')),
    ]
   ```
    * by adding the new path, we make the paths of rate.urls the main ones.
    * Then we import the functions of the controller in urls.py of rates module.
  ```
  from .views import *
  
  urlpatterns = [
    path('', index),
  ]
  ```
    * Adding a new path, we set the index function of the controller as the main road.

---

## Python Code In HTML

* Python syntax in html is written in parentheses: {{ }}
* We add {{ title }} to the < title > tag, which is the key written in the context directory of the index function.
* Then, we write for loop in table:

```html
               {% for i in bank %}

<tr>
    <td>{{ i.bank_name }}</td>
    <td>{{ i.usd_buy }}</td>
    <td>{{ i.usd_sell }}</td>
    <td>{{ i.eur_buy }}</td>
    <td>{{ i.eur_sell }}</td>
    <td>{{ i.rub_buy }}</td>
    <td>{{ i.rub_sell }}</td>
</tr>
{% endfor %}
```

* It loops through the value of the 'bank' key in the context dictionary and creates the table based on the database
  data.

---

## Run Server

![Screenshot (1)](https://user-images.githubusercontent.com/111388676/214602842-7728b58b-3f48-4327-a69e-8ca96690a03a.png)

* Header div contains bank names with a link to the respective bank's website.
* Below is the intro div, in which a table created with a for loop.

---

### (part 2)
* Exchange rates will be imported from the banks' websites and will be modified according the information provided the bank.
* By clicking on the names of the banks, new pages will be opened, where displayed information about the branches of the given bank.
