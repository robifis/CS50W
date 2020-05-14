
- [Lecture5 - SQL](#lecture5---sql)
  - [Introduction](#introduction)
    - [Data](#data)
    - [SQLite Types](#sqlite-types)
    - [MySQL Types](#mysql-types)
    - [Type Constraints](#type-constraints)
    - [SQL Commands](#sql-commands)
  - [SQL Databases](#sql-databases)
    - [Creating a database](#creating-a-database)
    - [Adding Data into Database](#adding-data-into-database)
    - [Getting Data out of the Database](#getting-data-out-of-the-database)
    - [Updating the database](#updating-the-database)
    - [Deleting items in Database](#deleting-items-in-database)
    - [Foreign Keys](#foreign-keys)
    - [Joining Databases](#joining-databases)
      - [JOIN Methods](#join-methods)
    - [CREATE INDEX](#create-index)
    - [SQL Injection](#sql-injection)
      - [Race Condition](#race-condition)
  - [Django Models](#django-models)
    - [Migrations](#migrations)
    - [Inserting Data](#inserting-data)
    - [Creating Flights](#creating-flights)
  - [Building a web application](#building-a-web-application)
    - [Accessing Airports](#accessing-airports)
    - [Creating new flights](#creating-new-flights)
  - [Django Admins App](#django-admins-app)
    - [Registering the models](#registering-the-models)
    - [Accessing individual flights (via ID)](#accessing-individual-flights-via-id)
      - [Dynamic url paths](#dynamic-url-paths)
      - [Displaying the data dynamically](#displaying-the-data-dynamically)
    - [Adding Passengers](#adding-passengers)
    - [Displaying Passengers for a Particular Flight](#displaying-passengers-for-a-particular-flight)
      - [Dynamic Links in Django](#dynamic-links-in-django)
    - [Passenger Booking System](#passenger-booking-system)
      - [Passenger Booking Form](#passenger-booking-form)
        - [Adding non-passengers](#adding-non-passengers)
    - [Customizing the Admin Page](#customizing-the-admin-page)
    - [User Login System](#user-login-system)
      - [Login](#login)
      - [Logout](#logout)

# Lecture5 - SQL

## Introduction

Python Classes are referred to as Models in SQL!
Migrations are techniques that allow us to make changes to the underlying database!

### Data

A relational database will have rows and columns.  

SQLite is the Django default!
Each database can store its own [type](#sqlite-types) depending on its use.

### SQLite Types

- Text
- Numeric
- Integer
- Real
- Blob (Binary Large Object)

### MySQL Types

- CHAR(size) => Fixed size of characters
- VARCHAR(size) => Variable size of characters (up to 'size')
- SMALLINT
- INT
- BIGINT
- FLOAT
- DOUBLE

### Type Constraints

- CHECK => Allows to check against a certain condition (Must be between 1 and 5)
- DEFAULT
- NOT NULL
- PRIMARY KEY
- UNIQUE => Must be a unique value in the column.

### SQL Commands

Let's have a look at how we would represent this table in SQLite

|origin|destination|duration|
|------|-----------|--------|
|New York|London|415|
|New York|Paris|450|
|London|Dubai|500|
|Vienna|Warsaw|120|

Here is how you would create a SQLite table (Our example is concerned with Flights)

```sql
CREATE TABLE flights(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL
    destination TEXT NOT NULL
    duration INTEGER NOT NULL
);
```

**id, origin, destination, duration**  
They are all the names of the columns.
It is often good practice to assign id's that are not unique to each item as there might be multiple entries that are the same. In our case, there might be multiple airlines who are flying from New York to London and it is important to be able to distinguish between them when querying the database. SQL will usually handle the id part automatically and add that itself so we don't have to.

**INTEGER, TEXT**  
They are types. This is what was discussed [above](#sqlite-types). That way the db knows what type it is storing. It could be an integer or a piece of text.

**PRIMARY, NOT NULL**  
They are constraints that we might add to each item. For example **Autoincrement** will increase the value automatically with each new item stored.
**Not Null** means that the value can't be blank.

## SQL Databases

### Creating a database

We can just use a simple command in order to create a database by typing in a particular command into our command line:

`touch filename.sql` => This will create a new database file

To enter a sqlite3 prompt, in order to manipulate the database, we type the following:
`sqlite3 filename.sql` => This command will open a new prompt for us to access the sqlite database.
Once inside of here, we can create the database with the commands that we looked at [here](#sql-commands)

**NOTE:**
We can query a database by using Regular Expressions if we're unsure of a certain line.
So we can do:
`SELECT * FROM flights WHERE origin LIKE "%a%";`
As long as there is an *a* inside of the *origin* column!

We can also use other function to query the database by using AVERAGE, COUNT, MAX, MIN, SUM etc... This is very similar to excel!

### Adding Data into Database

Data is added into the database via the INSERT command.

```sql
INSERT INTO flights
    (origin, destination, duration)
    VALUES('New York', 'London', 415);
```

The data that will be entered must be passed in via comma separated values(csv). This will populate each column, one by one.

### Getting Data out of the Database

To get data out of the database we use the SELECT command.

We can use `SELECT column_name` in order to get all the data out of a specific column.
To get a specific row we can use:
`SELECT * (meaning all) FROM flights (name of DB) WHERE id=3.`
This will return the id with the row number 3.

### Updating the database

This is how you update a database:

```sql
UPDATE flights
    SET duration = 430
    WHERE origin = "New York"
    AND destination = "London";
```

This command updates the flight time in our database between New York and London.
In plain english it looks as follow:
SQLite:
**UPDATE** the *flights* table and **SET** a *duration* of *430*, **WHERE** the *origin* is *New York* **AND** the *destination* is *London*.

### Deleting items in Database

The command to delete items in the database is:
`DELETE FROM flights WHERE destination="Tokyo";`
**DELETE** all the inputs in *flights* table **WHERE** the *destinations* is *Tokyo*.

### Foreign Keys

A foreign key is a reference to another table. We can use those to reference a particular data item from another table!

Once datasets become larger and larger we might want to separate out the data into multiple columns and sets. We can then reference these amongst each other. That way we don't have to hard code the data into tables.

Looking at the flights data in particular, we could separate out the airports themselves into a unique table.

|id|code|city|
|--|----|----|
|1 |JFK |New York|
|2 |PVG |Shanghai|
|3 |IST |Istanbul|
|4 |LHR |London|
|5 |SVO |Moscow|
|6 |LIM |Lima|
|7 |CDG |Paris|
|8 |NRT |Tokyo|

We can change this table and replace it with a table that has foreign keys.
It would look like this:

|id|origin_id|destination_id|duration|
|-|-|-|---|
|1|1|4|415|
|2|1|7|450|
|3|4|9|500|
|4|6|5|120|

Once we create separate tables where we associate unique ids to individual items we can then create associated tables where we reference items from one table and associate them to another table, without hardcoding any values into them.

### Joining Databases

SQL allows us to join multiple queries together in order to be able to see data. If we're only using unique ID's then it's difficult to see the data properly and it doesn't make things immediately obvious.
Such a **JOIN** query could look like this

```sql
SELECT first, origin, destination
    FROM flights JOIN passengers
    ON passengers.flight_id = flights.id
```

**SELECT** tells sql what data we need (first, origin and destination)
**FROM** tells sql what table to use
**JOIN** tells sql what table want to join it with (passengers in this case)
**ON** tells sql how the two tables are related to each other.

So we're telling sql that the *flight_id* for each passenger is related to the *flights.id* (Note: flight_id and flights.id)
*passenger.flight_id* = the flight the passenger is on
*flights.id* = a particular flight (has an origin and a destination)

Using the **JOIN** keyword allows us to then create tables that are much easier to read (for humans) but also allows us to create tables at will without having to manually create a new table!

This is what the final table would look like
|first|origin|destination|
|-|-|-|
|Harry|New York|London|
|Ron|New York|London|
|Hermione|Shanghai|Paris|
|Draco|New York|Paris|
|Luna|Lima|New York|
|Ginny|Lima|New York|

#### JOIN Methods

- JOIN / INNER JOIN => This is the one we have used where the conditions have to match!
- LEFT OUTER JOIN
- RIGHT OUTER JOIN
- FULL OUTER JOIN

### CREATE INDEX

We can also create an index of all the data which makes querying the data much easier in the long run but it requires additional memory and maintenance.
Think of an index like the index in a book. You can go to the back and look for a word and it will tell you the location of it inside of the book.

```sql
CREATE INDEX name_index ON passengers (last);
```

### SQL Injection

SQL Injections are a security vulnerability where a hacker might gain access to a database.

Making comments in sql is done via --. A hacker could potentially try and log in to the database and trick the system by writing a specific username containing --. This would allow you to bypass the password check.
A normal query looks like this
`SELECT * FROM users WHERE username="username" AND password = "password";`

If a hacker adds the -- lines then they might bypass the Password check and log in as the password check is effectively "commented out".
`SELECT * FROM users WHERE username="hacker" --" AND password = "";`
Everything from after the -- is effectively commented out!

Using Django allows us to write sql syntax but without having to know and understand it directly and Django also provides an extra layer of security for us by writing it for us!

#### Race Condition

A race condition is when multiple checks/threads etc are happening simultaneously. One example would be cthat if two users were trying to see how many likes there are on particular twitter post, for example.

To avoid these potential problems would be to add a "lock" so that when somebody is working on the database we won't allow anyone else to work on it until the initial person if finished with their work.

## Django Models

In order for us to be able to use sql inside of Django, we need to create models. Models are classes, as referred to [here](#introduction), inside of Django that allow us to create a database.

We need to create our database inside of `project_folder > models.py` file.

Similar to our example regarding flights, we can now create a Flight class, that stores the origin, the destination and the duration:

```python
from django.db import models

class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}
```

We can then define a `__str__` inside of the class so the data we get back if query it looks much nicer. `__str__` is called a string representation. It essentially means that we want it represent the output in a string format that we define.

The argument inside of the class function is models.Model where we inherit a function from the models file.
We also define the [types](#mysql-types) for each item and add some [constraints](#type-constraints) in order to limit the fields.

### Migrations

Once we've created our model, we need to update Django and "migrate" our data. By migrate we mean that we need to update Django to create a new database.

First we need to run the following command:
`python manage.py makemigrations`

This command will create a folder called  `migration` inside of the `project_folder`. Inside of that we will find a filename called `0001_initial.py`.  
The model will have the name of the Class we have created inside of the `models.py` file ("Flight" in our case).

This file will create all the instructions to Django on how to manipulate the database.
**NOTE**: THIS WILL ALSO CREATE AND ADD A UNIQUE ID FIELD. WE DON'T NEED TO ADD THAT ANY MORE!

Once we've done that we need to apply those migrations by running the following command:
`python manage.py migrate`
This will effectively create our table.

**Summary:**  
To create a database in Django it's a two step process:

1. `python manage.py makemigrations` => Creates 0001_initial.py file
2. `python manage.py migrate` => Creates db.sqlite3 file inside of the main project

### Inserting Data

We are now in a position where we can insert data into our database.

One of the things discussed is that instead of hardcoding the data into a database, we can use [Foreign Keys](#foreign-keys) to represent another database.

To do this, we need to create another class inside of the `models.py` file, above the Flight Class:

```python
from django.db import models

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}
```

As you can see, because we've created the Airport class, we can now link it to the Flight model by adding a Foreign Key to the origin variable.
It now reads `origin = models.ForeignKey(Airport, on_delete = models.CASCADE)` instead of `origin = models.CharField(max_length=64)`.

The first argument inside of the bracket refers to the name of the class we want to link to, which in our case is Airport.

The second argument `on_delete = models.CASCADE` means that if we ever delete an airport from the database, such as JFK, we want it to delete any other items that also reference JFK. Cascade down, essentially.

The third argument, is `related_name` which allows me to access a relationship in reverse order. I can access a flight by accessing `Flight.origin` but this argument allows me to access all the flights that have this airport as an origin. "Departures" will allow me to access all the flights leaving that airport.
We can also do the same for our destination field, where we link the Airport class to the Flight class, but we can also add related_name, in order to be able to see the arrivals at that particular airport.

So creating the related names allows me to not only see the origin and destination (and duration) of a particular flight but I am also able to query all of the flights going out of that airport and into the arrival airport.

As before, we need to run the two commands that [confirm the changes](#migrations):

1. Run the following command:
`python manage.py makemigrations`
2. Once we've done that we need to apply those migrations by running the following command:
`python manage.py migrate`

### Creating Flights

Now that we have those two classes, we can create airports and link them to flights:

Creating an Airport is the same as creating a Class:

```sql
jfk = Airport(code='JFK', city='New York')
jfk.save()
lhr = Airport(code='LHR', city='London')
lhr.save()
cdg = (Airport(code='CDG', city='Paris')
cdg.save()
nrt = Airport(code='NRT', city='Tokyo')
nrt.save()
```

Now to create a flight:

```sql
f = Flight(origin=jfk, destination=lhr, duration=415)
f.save()
```

This is the simplified version to create airports and flights but they important part is that we have created airports and linked them automatically to a flight via a Foreign Key.

We can now query items from another database:

```sql
f.origin
# <Airport: New York (JFK)> Exactly how we have defined it in the __str__ function inside of Airport!
f.origin.city
# 'New York'
f.origin.code
# 'JFK'
```

Because we have added the related_name argument we can also do the following:

```sql
lhr.arrivals.all()
<QuerySet[<Flight: 1: New York (JFK) to London (LHR)>]>
```

This will now show us all the arrivals into that particular airport!

## Building a web application

Django and SQL work together in order for us to be able to use "normal" python code and interact with the classes, instead of having to remember all the sql syntax and commands.
We can now, effectively create a view in our app and, as it is in our case, display all the flights.

A sample `views.py` function could look like this:

```python
from django.shortcuts import render
from .models import Flight # Here we are importing our Flight Database

def index(request):
  return render(request, 'flights/index.html', {
    'flights`: Flight.objects.all()
  })
```

We first import the Flight class from .models in order to have access to it.

We then create our function, as normal, and point it to our html file inside of the `app_name/templates/flights/` folder.
We can then pass in all of the flights to the html file via our 'flights' key (where the value is `Flights.object.all()`)
This essentially gives us access to everything we've created above!

We can then loop over the variable (flights in our case) as normal from within the HTML file.
We have access to everything from inside of the class so:

- flight.id
- flight.origin
- flight.destination

This is how we would display the data in a html file dynamically.

### Accessing Airports

We can access individual items from within a dataset via specific sql commands.
The commands are as follows:
If we want all of the Airports stored we can do:

- `Airport.objects.filter(city='New York')` => This will list all of the airports that have city set as 'New York'
- `Airport.objects.filter(city='New York').first()` => This will only display the first in the list of items that I have searched for.
- `Airport.objects.get(city='New York')` => This will only return me one item. It's useful to use this if we know that there is only one item in the list with that name.

### Creating new flights

We can now create new flights by storing the airport names in variables and then creating a new Flight by storing it in our Class via the airports.
We can do:

```sql
jfk = Airport.objects.get(city='New York')
cdg = Airport.objects.get(city='Paris')

f = Flight(origin=jfk, destination=cdg, duration=435)
f.save()
```

We have stored both airports in a variable and then created a new instance of the class by using the Airport Objects in order to create a new flight from New York to Paris.

This will now automatically, and dynamically, update our html and display the new flight in our list.

## Django Admins App

Because manipulating, adding and creating data and databases is that common within Django, Django actually has an app that already allows us to do that stuff with its built in models.

If we look inside of the project directory, inside of the `urls.py` file, we see that there is a path already there, called admin.
To access it, we first need to create a superuser via the command:
`python manage.py createsuperuser`
This will then ask us to create a username, email and a password.

### Registering the models

Once we have set up our superuser, we need to register our models so that our admin can access them.

Inside our `admin.py` file of our app, we need to write the following:

```python
from django.contrib import admin (this is here by default)

from .models import Flight, Airport (we need to add this)

# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight)
```

This will now all our Admin to access the classes created [earlier](#inserting-data).

We can now access the admin interface by going to:
`localhost:8000/admin`
This will prompt us for a login and we need to use the credentials that we have set up [here](#django-admins-app)

Once we're in here, we can manipulate(add, edit, delete) our data from inside of the admin interface, without having to do it like we did [here](#creating-new-flights)

Django is clever in the sense that when it comes to creating a new flight, for example, it will list all the airports in a dropdown menu for us, so we don't have type it in manually every time. It displays the same fields that we have created inside of our classes, such as Origin, Destination and Duration.
This makes data entry a lot easier.

### Accessing individual flights (via ID)

Django gives us the ability, via dynamic urls, to access specific data based on the id of the item. In our case, we want to access a particular flight via the id.

#### Dynamic url paths

To do this, we need to create a dynamic path inside of our `urls.py` file within our app.

```python
urlpatterns = [
    path('', views.index, name='index')
    path('<int:flight_id>', views.flight, name='flight')
]
```

The second path is the dynamic url, which will allow us to access each flight by their own individual flight_id's.

We now, of course, need to create the flight function, inside of the `views.py` file (views.flight)

```python
def flight (request, flight_id):
  flight = Flight.objects.get(id=flight_id)
  return render(request, 'flights/flight.html`, {
    'flight': flight
  })
```

The code above will do the following:
First it will get the flight with the specific id that we have told it to search and store it in the variable called 'flight'. It will then render get the specific html file (flight.html). We also pass it a dictionary into the html via the `flight`:flight parameter. We're passing it the data that's stored in the variable
`flight=Flight.objects.get(id=flight_id)`
This variable contains all the data from the flight, meaning we can get the origin, the destination and the duration of the flight.

#### Displaying the data dynamically

We can then display all of this data inside of the html:

```html
{% extends 'flights/layout.html %}

{% block body %}
  <h1>Flight {{ flight.id }}</h1>

  <ul>
    <li>Origin: {{ flight.origin }}</li>
    <li>Destination: {{ flight.destination }}</li>
    <li>Duration: {{ flight.duration }}</li>
  </ul>

{% endblock %}
```

This is how we would display the content of each flight individually via a dynamic page. We don't need to create a new page for each flight. We will just let Django create it for us dynamically!

### Adding Passengers

First, we need to create another Model for our passengers.
For that, we need to add the class to our models.py file with passenger attributes.

```python
class Passenger(models.Model):
  first = models.CharField(max_length=64)
  last = models.CharField(max_length=64)
  flights = models.ManyToManyField(Flight, blank=True, related_name='passengers')

  def __str__(self):
    return f"{self.first} {self.last}
```

So here we have created new Class to create passengers. We can also assign a field to them that's `models.ManyToManyField` where we add the Flight list (meaning that they can be on multiple flights,), `blank=True` means that they might not have a flight associated with them and then finally we add `related_name = passengers` so we can query that if we only have a destination, for example and we wanted to see who is going there.

Lastly, after every group that we create we need to apply those changes:

```sql
1. python manage.py makemigrations
2. python manage.py migrate
```

This will commit all the changes.

We will still have to register our models in the `admin.py` file, like [here](#registering-the-models)

```python
from django.contrib import admin (this is here by default)

from .models import Flight, Airport, Passenger (we need to add this)

# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passenger)
```

This will give us access to the Passengers list from within the admin page!

### Displaying Passengers for a Particular Flight

We can display all the passengers on any given flight they're associated with by adding them dynamically to the flight function, inside our `views.py` file:

```python
def flight (request, flight_id):
  flight = Flight.objects.get(id=flight_id)
  passenger - flight.passengers.all()
  return render(request, 'flights/flight.html`, {
    'flight': flight,
    'passengers: passengers
  })
```

flight.passengers.all() => passengers is the related name we have given it! That's what gives us access to all the passengers!

So we're essentially accessing the flight variable and via dot notation `flights.passengers.all()`. Hence why we pass in related names!
However, we only have access to the flights for THAT particular flight with that particular id.

Our flight.html would look like this:

```html
{% extends 'flights/layout.html %}

{% block body %}
  <h1>Flight {{ flight.id }}</h1>

  <ul>
    <li>Origin: {{ flight.origin }}</li>
    <li>Destination: {{ flight.destination }}</li>
    <li>Duration: {{ flight.duration }}</li>
  </ul>

  <h2>Passenger List</h2>

  <ul>
    {% for passenger in passengers %}
      <li>{{ passenger }} </li>
    {% empty %}
      <li>No Passengers</li>
    {% endfor %}
  </ul>

  <a href="{% url 'index %}">Back to Flight List</a>

{% endblock %}
```

This will now dynamically show each passenger who is on that particular flight.

#### Dynamic Links in Django

As we've seen before with Django, we can link to a particular page via the {% url 'functionName %}

Inside of the `index.html` file we can also add links to each flight and we can create them dynamically:

```html
<a href="{% url 'flight' flight.id %}">
  Flight{{ flight.id }}: {{ flight.origin }} to {{  flight.destination }}
</a>
```

This will allow me to link to a specific flight when I click on it, based on it's flight id. This is also how you create dynamic links.

### Passenger Booking System

We are now in a position to be able to create a route that will allow me to book passengers onto a flight.
We first need to create a route inside of our app/urls.py file:

```python
urlpatterns = [
  path(""),views.index, name="index"),
  path("/<int:flight_id>"),views.flight, name="flight"),
  path("/<int:flight_id>/book"),views.book, name="book"),
]
```

Then we need to create the book function.
Remember, if we want to submit data, we need to make sure it is done so via a POST method.

```python
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger # important to import the models!

def book(request, flight_id):
  if request.method == 'POST':
    flight = Flight.objects.get(pk=flight_id)
    passenger =
    Passenger.objects.get(pk=int(request.POST['passenger']))
    passenger.flights.add(flight)

    return HttpResponseRedirect(reverse("flight", args=(flight.id, )))
```

`request.POST['passenger']` => This means that the data that will be passed into the form (POSTED) will come from a field with the name "passenger". The name on any input field is the name we will get.
NOTE: We need to convert it to an integer, as that's what the passenger ID will be.
We are storing the passenger inside of the variable that we have got from the from the booking form (We are booking an existing passenger onto a flight, not creating a new one!)

We are then adding the passenger to the flight object via `passenger.flights.add(flight)`
Finally, we are redirecting the user back to the flight page with that particular flight id.

#### Passenger Booking Form

It's now time to create the form but first we need to add another line inside of the flight function, inside of `views.py` to be able to only book passengers onto the the flight which aren't on the flight already.

We need to add this variable of our flight function

```sql
non_passengers: Passengers.objects.exclude(flights=flight).all()
```

Essentially, this variable will show me all the passengers that aren't on that particular flight.

Inside of the `flight.html` file we can create a dropdown menu for all the passengers that aren't already on the flight.

##### Adding non-passengers

```html
<form action="{% url 'book' flight.id %}" method="post">
{% csrf_token %}
<select name="passenger">
  {% for passenger in non_passengers %}
    <option value="{{ passenger.id }}">{{  passenger }}</option>
  {% endfor %}

<input type="submit">

</select>

</form>
```

Here we need to make sure we pass it the method of post and we also need to name the dropdown passenger, the same as what we've used inside of the book function `request.POST["passenger"]` so that the system knows where the name is coming from.

This dropdown will contain all the non_passengers, where we select the id as a value `{{ passenger.id }}` but we display the `{{ (non)passenger name }}` that we're looping over.

**Quick Summary:**
We have covered a lot in this part so let's break it down as to what has actually been done.

We have created a dynamic html file inside of our django project that is specific to each flight (by passing in an ID).
Inside of that page we are showing the flight, the current passengers along with a form that will allow me to add a passenger to the list from a list of non-passengers.

Once we add a passenger from the non-passenger list we get redirect back to the flight page and the name of the passenger disappears from the dropdown list too!

Technicalities:
If we look inside of the [form](#adding-non-passengers), we can see that the option value is the `passenger.id` yet we display the Passenger name via the variable we have received from inside of the python code.

### Customizing the Admin Page

Django allows us to customize the view of the Admin page.
We can have it display the data we want instead of having it display all of the information. There might be less relevant information in there that we might want to hide or information that we might want to be able to view.

Read more about customizing the Django Admin page [here](https://docs.djangoproject.com/en/3.0/ref/contrib/admin/)

If we want to adjust what we want it to display, we can create a new class inside of the `admin.py` file, the same file where we have registered all our views, such as passengers, airport and flight etc.

```python
class FlightAdmin(admin.ModelAdmin):
  list_display = ('id', 'origin', 'destination', 'duration')

admin.site.register(Flight, FlightAdmin)
```

The code above is broken down as follows. First we create a subclass of ModelAdmin (that's why it is an argument inside of the class).

We then create the view we want by amending the list_display.

Once done, we have to also add the FlightAdmin Class to the part where we register the FLight in order for us to "override" the default view.

### User Login System

#### Login

1. create a the way we always always would:
`python manage.py startapp users`
2. Add the app to installed apps
3. Include the path to the `urls.py` inside of the project
4. Create `urls.py` file inside of the app
5. Create views inside of `views.py`

For our login system we can create 3 views

First, let's create the index view that we usually create.
We will also have to create a login_view and a logout_view function (naming them "login" and "logout" respectively. )

```python
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Importing authentication functions (provided by Django)
from django.contrib.auth import authenticate, login, logout

def index(request):
  if not request.user.is_authenticated:
    return HttpResponseRedirect(reverse('login'))
  return render(request, 'users/user.html')
  # If the user was logged in successfully!

def login_view(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return HttpResponseRedirect(reverse('index'))
    else:
      return render(request, 'users/login.html', {
        'message':'Invalid credentials'
      })
  return render('users/login.html')
```

Inside of the index function, we have created a redirect to the login view, if the user is not authenticated, meaning that if he's not signed in then the function will automatically redirect him to the login page. The `request.user.is_authenticated` part is already baked into Django.

We need to create a form inside of the `login.html` file but we have to make sure that the data gets passed in via the POST method as the GET method shows the parameters inside of the URL. Important for when doing a login system!

`username = request.POST['username']` This line, same as before, means that the username will be provided via a field called 'username' inside of the POST field.

Django also provides us with functions that allow us to authenticate a user, log the user in and log the user out. They're imported separately via the `from django.contrib.auth import authenticate, login, logout`
`user = authenticate(request, username=username, password=password)` This line will check against the entered username and password in the submit form and if they can be authenticated against the users who are already inside of the admin database, we get back the user.

Logging a user is done via a built in Django function with a conditional to check if the user does exist (if user is not None). This will log the user in and then return them back the user page.

```python
if user is not None:
    login(request, user)
    return HttpResponseRedirect(reverse('index'))
```

If the user is not a current user we can then display a message that says that the user was not authenticated:

```python
else:
    return render(request, 'users/login.html', {
        'message':'Invalid credentials'
}
```

Because we've passed down a message inside of the else statement, we can display that message now on our login page to let the user know that they haven't been logged in.

Once the user has successfully been able to log in, we can display all their relevant information inside of the html file. We can do this because we have access to the request variable.
So we have access to things such as:

- request.user.username
- request.user.first_name
- request.user.email

#### Logout

Just as there is a login function, Django also provides a logout function.
We can create this quite simply and we just need to redirect the user back to a specific page once they've logged out successfully.

```python
def logout_view(request):
  logout(request):
  return render(request, 'users/login.html, {
    'message': 'Logged Out'
  })
```

Finally, we need to add a link to the logout route inside of the html file.
`<a href="{% url 'logout' %}">Log Out</a>`
This will point the link to the logout function inside of our views.py file for that particular app!
