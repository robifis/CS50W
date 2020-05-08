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

**Best Practices:**
- [Template Inheritance](#template_inheritance)

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

<a> name="links">Links</a>
First, we need to create a new file inside of the app folder called `urls.py`. This is important so that our app can link to individual routes within the app. 
The `urls.py` file needs to look as follows:

```
from django.urls import path # Similar to the urls.py file inside of the project file
from . import views # This imports the views.py file from the app folder (hence the .)

# Adding this above the urlpatterns patterns varibale will help django 
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

<a> name="views">Views</a>
We also need to create a new view(function) inside of the `views.py` file in the app folder. There is no difference if you create a link first or the view. The names have to match! 

This is what a function looks like:
```
def index(request):
    return render(request, 'app_name/index.html')
```
This is the simplest function that returns the index.html page from inside of the `app_name/templates/app_name/` folder. Here we store all our html files. 
We only need to specify any additional folders beyond the `templates` folder in our path. We don't need to specify templates! This helps to avoid naming conflicts!

**Optional**
We can create a base template that inherits the html that doesn't change(navbar, head, etc...). 
See [template inheritance](#template_inheritance) to read more.





#### <a name="template_inheritance">Template Inheritance</a>
### <a name=""></a>
### <a name=""></a>
### <a name=""></a>
