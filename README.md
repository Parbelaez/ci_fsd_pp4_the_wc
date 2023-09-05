# Django CRM

 A basic CRM developed in Django... aimed as a template for future projects.

## Project setup

### Install dependencies

First, it is needed to create a virtual environment, which is a folder that contains a Python installation and all the packages needed for the project. This is done by running the following command at the root of the project:

```Python
python3 -m venv .venv
```

**NOTE**: The name of the virtual environment folder is .venv, which is the default name. If you want to use a different name, you should add the name of the folder to the .gitignore file. Also, ```python3``` was used because the project was developed on a Mac. If you are using Windows, you should use ```python``` instead.

Then, the virtual environment is activated by running the following command:

```Python
source .venv/bin/activate
```

Finally, the dependencies are installed by running the following command:

```Python
pip3 install django gunicorn dj_database_url dj3-cloudinary-storage urllib3 psycopg2 django-summernote django-allauth django-crispy-forms
```

**Django**, is the main framework used to create the application. It allows the developer to create a web app using Python.
**Gunicorn** is a web server that is used to deploy the application to Heroku. dj_database_url is a package that allows the developer to connect to a database. **dj3-cloudinary-storage** is a package that allows the developer to connect to Cloudinary, which is a cloud-based image and video management service.
**urllib3** is a package that allows the developer to make HTTP requests.
**psycopg2** is a package that allows the developer to connect to a PostgreSQL database.
**django-summernote** is a package that allows the developer to add a rich text editor to the application.

### Create the environment variables

First, create a env.py file in the root of the project with the following variables:

```Python
import os   # for os.environ.get

# Set the environment variables
os.environ["DATABASE_URL"]='YOUR_DB_URL'
os.environ["SECRET_KEY"]='YOUR_SCRET_KEY!'
# If you will work with images or static files, you will need to set the following variable
os.environ["CLOUDINARY_URL"]="YOUR_CLOUDINARY_URL"
```

**NOTE:** The env.py file is not pushed to GitHub because it contains sensitive information. Therefore, if you want to run the project locally, you need to create your own env.py file.

Then, add the env.py file to the .gitignore file, so it is not pushed to GitHub.

### Create a Django project

**NOTE:** Please, be aware that one thing is the project and another thing is the application. The project is the whole thing, while the application is a part of the project. In this case, the project is called *ci-fsd-blog* and the application is called *blog*.

A Django project is created by running the following command:

```shell
django-admin startproject ci_fsd_pp4_the_wc .
# The dot at the end is important because it tells Django to create the project in the current directory.
```

But, Django also needs to know where to get the variables from, therefore, the following lines are added to the settings.py file:

```Python
import os
import dj_database_url

if os.path.isfile("env.py"):
    import env
```
An app's name should follow [Pep 8 Guidelines](https://www.python.org/dev/peps/pep-0008/#package-and-module-names), namely it should be short, all-lowercase and not include numbers, dashes, periods, spaces, or special characters. It also, in general, should be the plural of an app's main model, so our posts app would have a main model called Post.

A Django application is created by running the following command:

```shell
python3 manage.py startapp thewcwebpage
```

Then, the application is added to the project by adding the following line to the INSTALLED_APPS list in the settings.py file:

```Python
'thewcwebpage',
```

Create the static and templates folders in the root folder by running the following commands:

```shell
mkdir static
mkdir templates
```

To create the templates for the registration and login pages, the following command is run:
(All these will be used later, but it is better to have everything ready.)

```shell
cp -r ./.venv/lib/python3.11/site-packages/allauth/templates/* ./templates
```

This will copy all the templates from the allauth package to the templates folder.


### DB Configuration

Remember that you already installed dj_database_url, which is a package that allows the developer to connect to a database. Also, you have already declare your environment variable for the database in the env.py file.

Therefore, you need to add the following lines to the settings.py file:

```Python
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
```
### Migrations

Everytime a change is made to the models (db structure), it is needed to run the following commands:

```shell
python3 manage.py makemigrations
python3 manage.py migrate
```
...and as we created all necessary setup to be able to run a DB in the project, we need to run the commands above.

At this point, you should be able to see some tables in the DB.

We are using Elephant SQL as our DB provider, and we are using the free tier, which is limited to 20MB. Therefore, we need to be careful with the amount of data we store in the DB.

And the tables can be accessed here:

[Elephant SQL](./README%20images/elephantSQL_browser.png)

and can be queried here:

[Elephant SQL](./README%20images/elephantSQL_query.png)

### Create a superuser

To be able to access the admin panel, it is needed to create a superuser by running the following command:

```shell
python3 manage.py createsuperuser
```

You will be asked for your username, email and password. This will be the user that will be able to access the admin panel.

### Initial deployment to Heroku

As the project will be deployed in Heroku, after installing the dependencies, it is needed to create a requirements.txt file by running the following command:

```shell
pip3 freeze > requirements.txt
```

This file will contain all the dependencies installed in the project, and will be used by Heroku to install them when the project is deployed.

Now, it is needed to create a Procfile, which is a file that tells Heroku what to do when the project is deployed. This is done by running the following command:

```Shell
echo web: gunicorn django_crm.wsgi:application > Procfile
```

### Add the app file to your urls definition

To be able to access the app, it is needed to add the app file to the urls definition in the urls.py file. This is done by adding the following line to the urlpatterns list:

```Python
path('', include('app_crm.urls')),
```

### Create the app urls

But it is the app actually, the one accessing urls. Therefore, it is needed to create the app urls by creating a urls.py file in the app folder and adding the following lines:

```Python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

### Create the models

The models are created in the models.py file. In this case, the models are:



## The design of the webpage and app

For most of the styling, Bootstrap was used, and some customization was done in the style.css file.

### The base template

The base template is the template that is used by all the other templates. It contains the header, the footer and the navbar. It also contains the links to the Bootstrap and jQuery libraries.

But, as it can be seen, the header is a nav bar, therefore, it was created sepparately in the navbar.html file, and then it was included in the base.html file by adding the following line:

```HTML
{% include 'navbar.html' %}
```

### The navbar

The navbar is a Bootstrap navbar, and it is created in the navbar.html file. It contains the links to the different pages of the app, and it also contains the links to the login and registration pages.

### The home page

The home page is the page that is shown when the user first enters the webpage. It contains a carousel with some images, and it also contains a section with some information about the company.

For the login process, no new webpage was created. Instead, it was included in the home screen as a modal. This was done by adding the following lines to the home.html file:

```HTML
{% include 'account/login.html' %}
```

For the logout, a new webpage was created, and it was added to the navbar. This was done by adding the following lines to the navbar.html file:

```HTML
<li class="nav-item">
    <a class="nav-link" href="{% url 'logout' %}">Logout</a>
</li>
```

For the register, also a new webpage was created, and the form was crated directly with Django. The reason behind this is that we need some extra fields and controls on them, like: the password confirmation, the email confirmation, the captcha, and the password rules (number of characters, and so on...).


*NOTE:* as seen in the comments of the views.py file, the password field must be gotten using the get method, and not the post method. This is because Django does not allow to get the password using the post method (reported bug).


### OPTIONAL: Captcha and crispy forms

The captcha was added by using the django-simple-captcha package. To install it, run the following command:

```shell
pip3 install django-simple-captcha
```

Then, add the following line to the INSTALLED_APPS list in the settings.py file:

```Python
'captcha',
```

And, add the following lines to the settings.py file:

```Python
CAPTCHA_LENGTH = 6
CAPTCHA_FONT_SIZE = 30
CAPTCHA_LETTER_ROTATION = (-35, 35)
CAPTCHA_BACKGROUND_COLOR = '#ffffff'
CAPTCHA_FOREGROUND_COLOR = '#000000'
CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_dots',)
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
CAPTCHA_OUTPUT_FORMAT = u'%(image)s %(hidden_field)s %(text_field)s'
```

To be able to use the captcha in the registration form, it is needed to add the following lines to the register.html file:

```HTML
{% load captcha %}
{% captcha_image %}
{% captcha_hidden_field %}
{% captcha_text_field %}
```


To be able to manage the comments and have a proper interface to do so, you need to install crispy forms by running the following command:

```shell
pip3 install django-crispy-forms
```

Then, you need to add the 'crispy-forms' line to the INSTALLED_APPS list in the settings.py file.

And, as we will be using Bootstrap for these forms, then it is needed to declare the following line in the settings.py file:

```Python
CRISPY_TEMPLATE_PACK = 'bootstrap4'
```

NOTE: As of django-crispy-forms 2.0 the template packs are now in separate packages.

You will need to pip install crispy-bootstrap4 and add crispy_bootstrap4 to your list of INSTALLED_APPS.


### Create the models (DB structure)

The models are created in the models.py file. In this case, the models are:

* Record: this is users table, which in Django is treated as a Python Class. So, basically, after creating a class, Django will create an object during the makemigrations process. Which is then used to create the table in the database during the migrate process.

But, the table is not yet accessible in the admin panel. To do so, it is needed to create a superuser by running the following command (already done):

```shell
python3 manage.py createsuperuser
```

Then, it is needed to register the model in the admin.py file by adding the following lines:

```Python
from .models import Record
```

Django will automatically pluralize the name of the model, so it will be Records in the admin panel.

[Django models](./README%20images/models.png)

And, will create the table in the database.

[Postgres DB](./README%20images/DB.png)


### View the records in the website

To be able to view the records in the website, it is needed to create a view in the views.py file. This is done by adding the following lines:

```Python
from .models import Record

def records(request):
    """ A view to return the records page """

    records = Record.objects.all()

    context = {
        'records': records,
    }

    return render(request, 'records/records.html', context)
```

*NOTE:* in the views file in this project, the records are rendered in the home page, but this is not the best practice. The best practice is to create a new page for the records, and render them there. So, differences in the code may be found.

Then, it is needed to create the records.html file in the templates/records folder. This is done by running the following command:

```shell
touch templates/records/records.html
```

And, it is needed to add the following lines to the urls.py file:

```Python
path('records/', views.records, name='records'),
```

## Deployment -Heroku-

### Create a Heroku account

First, it is needed to create a Heroku account. This is done by going to the [Heroku website](https://www.heroku.com/) and clicking on the Sign Up button.

### Install Heroku

Then, it is needed to install Heroku. This is done by running the following command:

```shell
npm install -g heroku
```

### Install the Heroku CLI

Then, it is needed to install the Heroku CLI. This is done by running the following command:

```shell
brew tap heroku/brew && brew install heroku
```

### Install django-heroku

Then, it is needed to install django-heroku. This is done by running the following command:

```shell
pip3 install django-heroku
```

### Create a Procfile

Then, it is needed to create a Procfile. This is done by running the following command:

```shell
echo web: gunicorn django_crm.wsgi:application > Procfile
```

### Create a requirements.txt file

Then, it is needed to create a requirements.txt file. This is done by running the following command:

```shell
pip3 freeze > requirements.txt
```

### Install python-decouple

Then, it is needed to install python-decouple. This is done by running the following command:

```shell
pip3 install python-decouple
```


### Login to Heroku

Then, it is needed to login to Heroku. This is done by running the following command:

```shell
heroku login
```

### Create a Heroku app

Then, it is needed to create a Heroku app. This is done by running the following command:

```shell
heroku create
```

### Add the environment variables to Heroku

Then, it is needed to add the environment variables to Heroku. This is done by running the following command:

```shell

