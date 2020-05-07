# We need to import this inside of the app in order to be able to link within our app. This also allows us to extend the link from the main urls.py file that's inside of the project.
from django.urls import path
from . import views # We're importing the views.py file, we just don't write views.py. The . is that the file is in the same directory!

urlpatterns = [
    path("", views.index, name="index"),
    path("test", views.test, name="test")
]

"""
- path is just the name of the function. 
- views is the views.py file we've got inside the directory!
- index is the name of the function in the views.py file!
We're essentially telling django to look into the views.py file and run the "def index(request)" function!
- "/test" is a new function and we can have it display other things if the users requests url.com/blog/test

"""

