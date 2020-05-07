from django.shortcuts import render
from django.http import HttpResponse

"""
The views page inside of our new app will allow us to 
create the dynamic files we want our users to be able to see. 
"""

def index(request):
    return HttpResponse('<h1>Hello, World. This is my first Django Page!</h1>')

def test(request):
    return HttpResponse('This is now a test page!')

"""
We can now create as many routes as we want in here by creating different function.
We always need to be mindful to add them to the urls.py file inside 
of your app (not the project urls.py)
"""