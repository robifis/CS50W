# Lecture 4 - Django

Django is very unique in the sense that it will allow us to create a dynamic page with dynamic content. 
The other thing that is unique to Django is that we can create separate "apps" within the main project directory, allowing us to run them almost independently. The great thing is that we can port the whole app into another project if we need to - saving time. 

## TODO List

**How To:**
1. [Creating a new Django project + Initial Setup](#Create_App)
2. [Creating a new App](#new_app)
3. [Creating our first View](#create_links)  
3a. [Links](#links)  
3b. [Views](#views)
4. [Variables](#variables)

**Best Practices:**
- [Template Inheritance](#template_inheritance)
- [Static Files](#static_files)  
- [Urls in Django](#url_links)  
- [Sessions](#sessions)
  

### <a name="Create_App">Creating a new Django project + Initial Setup</a> 
We first need to create the django app by running the command `django-admin startproject Project_Name`. 
This will initiate the app and install all the necessary files for us. 
Inside a re 2 important files, `settings.py` which contains all the important settings for our project.
`manage.py` is another file that's important as it is the file that will allow us to execute commands via the command line. 
The `manage.py` file is inside of the root directory of the app. Whereas `settings.py` and `urls.py` is inside of the app folder. 
We will also have to modify the `urls.py`. It is like the table of contents of our app. It will allow us to link to other routes.

We also need to add the project to the `INSTALLED_APPS` variable that's inside of the `settings.py` file(inside of the root project folder!)

The command `python manage.py runserver` will allow us to start the development server and it will auto refresh so we can see our changes on the fly. It will run in `localhost:8000`. 

**NOTE:**
This only needs to be done for each new app created! We do not need to do this for every new page we create inside of the app!


### <a name="new_app">Creating a new app</a>
To create a new app, we issue the following command:
`python manage.py startapp App_Name` => We need to name the app. Things like blog, about, profiles etc...
This command will create a new directory inside of the django project folder, preloaded with pretty much all the necessary files we need in order for our app to work. We will now have to link the app by adjusting a variable inside of the `urls.py` file of our project app. 

In order to link the two files, open the `urls.py` file inside of the project directory (NOT THE NEWLY CREATED APP FOLDER!) and add the following inside of the `urlpatterns` variable. 
(We also have to import 'include' in order to be able to link to the app!)
```
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_name/', include('app_name.urls'))
    # We need to add this line in order to link the app to the project. It will tell Django the urls it has to follow!
]
```
The `app_name/` at the beginning must match the name of the app we've jut created. That tells Django where to look(which folder to look inside.). The second argument of the path function is tells Django to include all the urls that are in the `app_name/urls.py` file. This is where we will create routes within the app(NOT PROJECT) itself.  

**NOTE:**
This only needs to be done for each new app created! We do not need to do this for every new page we create inside of the app!

### <a name="create_links">Create links inside of the App</a>

Now that we've set up the project folder we need to create our first view in order to display something to our user when they come to the url. 

#### <a name="links">Links</a>
First, we need to create a new file inside of the app folder called `urls.py`. This is important so that our app can link to individual routes within the app. 
The `urls.py` file needs to look as follows:

```
from django.urls import path # Similar to the urls.py file inside of the project file
from . import views # This imports the views.py file from the app folder (hence the .)

# Adding this above the urlpatterns patterns variable will help django 
# link back to the function in order (in case there are naming conflicts)

app_name = 'app_name'
urlpatterns =[
    path("", views.index, name='index') 
] 

```
This is our first view, which links to the function called index inside of the views.py file!  
**""** => This is our "root" url. So if the user visits just www.url.com/app_name/  
**views.** => is the name of the file (views.py)  
**index** => is the name of the function.   
**name='index'** makes it easier to link between files later.   

#### <a name="views">Views</a>
We also need to create a new view(function) inside of the `views.py` file in the app folder. There is no difference if you create a link first or the view. The names have to match! 

This is what a function looks like:
```
def index(request):
    return render(request, 'app_name/index.html')
```
This is the simplest function that returns the index.html page from inside of the `app_name/templates/app_name/` folder. Here we store all our html files. 

The function name(`def index`) must match the name inside of the `urls.py` file that we have created.
So `def index` must match `views.index`. We are essentially telling urls.py to render what's inside of the `views.py` file. 
More specifically inside of the index function. 

We only need to specify any additional folders beyond the `templates` folder in our path. We don't need to specify templates! This helps to avoid naming conflicts!

**Optional**  
We can create a base template that inherits the html that doesn't change(navbar, head, etc...). 
See [template inheritance](#template_inheritance) to read more.

### <a name="variables">Variables</a>

Any modern website these days needs to be able to display dynamic content with the help of variables.
In django, variables are passed down via a dictionary. 

Example:
```
def sampleFunction(request, variable):
    return render(request, 'app_name/sampleFunction.html, {
        'variable': variable
    })
```

The "key" of the dictionary is the name of the variable that the HTML file will have access to.
The value is the value from the python code. 
This allows us to render and pass information to the HTML file from Python. 


#### <a name="template_inheritance">Template Inheritance</a>
Template inheritance is a best practice when it comes to creating websites in Django. 
We could easily render each HTML file manually but Django allows us to only only render the parts that we need in order to reuse code.

**How To:**  
We first need to create a base html file inside of the `app_name/templates/app_name` folder. 
This follows a typical naming patter which is either `base.html` or `layout.html`.

This file contains all the static data that won't change from page to page. 
It may contain things like the navbar, a link to our CSS stylesheet, a link to our Javascript files etc.

```
<html>
    <head>
        {% load static %}
        <title>Website Title</title>
        <link rel="stylesheet href="{% static '/app_name/style.css' %}">
    </head>
    <body>
        <nav>
            <li><a href="{% url 'index' %}">Home</li>
            <li><a href="{% url 'about' %}">About</li>
            <li><a href="{% url 'contact' %}">Contact</li>
        </nav>
        {% block body %}
        {% endblock %}
    </body>
</html>
```
This is what a basic layout page would look like (base.html or layout.html).
We can see a couple of differences in here though. We have a {% load static %} file (more on using static files [here](#static_files)).

Links are also handled slightly differently in Django vs normal HTML. 
More on links[here](#url_links).

**Dynamic Content**  
Dynamic content is displayed via blocks in Django (block body - endblock).
This block tells django that we only want it to render what's inside of that part from other websites.

Here is what the `index.html` (for example) home page would look like:
```
{% extends 'base.html' %}

{% block body %}
    Dyanamic HTML content goes here! 
{% endblock %}
```
This design makes for much cleaner code which is much more reusable!
All we did was tell Django what file we would like to extend (base.html) and then we just added everything we wanted to be different inside of the `{% block body  %} {% endblock %}` sections. 

We don't have to call it "body" we can call it anything we want. Especially useful if we want different areas with dynamic content.

#### <a name="static_files">Static Files (CSS, etc...)</a>
Loading static files is slightly different inside of a Django app when compared to normal html.
Static files, similar to HTML files are kept inside of the app_name/static/app_name folder. 
Again, because we write {% load static %} at the top of the page, Django knows to look inside of the static folder of the app.
We then need to specify any path inside of that static folder. 
It is helpful to create a folder inside of the static folder in order to avoid naming clashes!

Here is an example of loading `styles.css` from inside of the static folder:

```
{% load static %}
<link rel="stylesheet href="{% static '/app_name/style.css' %}">
```
We just need to make sure we specify `static` at the beginning before we link the file!

#### <a name="url_links">Urls in Django</a>
Django is powerful enough to allow us to create dynamic links to websites within our app. This has many benefits.
In order to create this we write the following code inside oft he href part:
```
<li><a href="{% url 'app_name:index' %}">Home</li>
```
Here 'url' simply tells django that we want go to the url path that has `name='index'` in it. This is why we add
names to paths inside of the `urls.py` file inside of the app directory!
To avoid issues with the url function we can prepend the name with the name we have defined inside of the `urls.py` file
inside of the app folder: `app_name:index`. This helps Django guide us to the correct url, in case there are other functions with the same name!

#### <a name="sessions">Sessions</a>

Sessions in Django allow us to create individual session for individual users. Django already stores a secure key for us so we don't have to worry about the security. It helps with validation too. 

#### <a name="redirect">Redirects</a>

Django also allows to create redirects and reverse engineer a url. This is particularly useful if we want to direct a user to a specific page after they've either filled out a form or logged in.

Inside of the `views.py` file we need to import the following:
```
from django.http import HttpResponseRedirect
from django.urls import reverse

return HttpResponseRedirect(reverse('app_name:index))
```
This can be added to any function where we want the redirect to apply. Note that we're still using the same convetion as described in the [Urls in Django](#url_links) section by adding the app name before the function. Again, this is to avoid naming conflicts!