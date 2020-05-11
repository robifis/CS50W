# Lecture5 - SQL

- [Lecture5 - SQL](#lecture5---sql)
  - [Introduction](#introduction)
    - [Data](#data)
    - [SQLite Types:](#sqlite-types)
    - [MySQL Types:](#mysql-types)
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

## Introduction

Python Classes are referred ti as Models in SQL!
Migrations are techniques that allow us to make changes to the underlying database! 

### Data
A relational database will have rows and columns.  

SQLite is the Django default! 
Each database can store its own type depending on its use. 

### SQLite Types:
- Text
- Numeric
- Integer
- Real
- Blob (Binary Large Object)

### MySQL Types:
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

|origin   |destination|duration|
|---------|-----------|--------|
|New York |London     |415     |
|New York |Paris      |450     |
|London   |Dubai      |500     |
|Vienna   |Warsaw     |120     | 

Here is how you would create a SQLite table:
```
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
They are types. This is what was discussed [above](#sqlite-types). That way the db knows what kind type it is storing. 

**PRIMARY, NOT NULL**  
They are constraints that we might add to the columns. So **Autoincrement** will increase the value automatically with each new item stored. 
**Not Null** means that the value can't be blank. 

## SQL Databases

### Creating a database

We can just use a simple command in order to create a database by typing in a particular command into our commandline:
`touch filename.sql` => This will create a new database file
To enter a sqlite3 prompt, in order to manipulate the database, we type the following:
`sqlite3 filename.sql` => This command will open a new prompt for us to access the sqlite database.
Once inside of here, we can create the database with the commands that we looked at [here](#sql-commands) 

NOTE:
We can query a database by using Regular Expressions if we're unsure of a certain line. 
So we can do:
`SELECT * FROM flights WHERE origin LIKE "%a%";`
As long as there is an *a* inside of the *origin* column!

We can also use other function to query the database by using AVERAGE, COUNT, MAX, MIN, SUM etc... This is very similar to excel!

### Adding Data into Database
Data is added into the database via the INSERT command.

```
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
```
UPDATE flights
    SET duration = 430
    WHERE origin = "New York"
    AND destination = "London";
```

This command updates the flight time in our database between New York and London. 
In plain english it looks as follow:
SQLite, **UPDATE** the *flights* table and **SET** a *duration* of *430*, **WHERE** the *origin* is *New York* **AND** the *destination* is *London*. 

### Deleting items in Database

The command to delete items in the database is:
`DELETE FROM flights WHERE destination="Tokyo";`
This command will **DELETE** all the inputs in *flights* table **WHERE** the *destinations* is *Tokyo*.

### Foreign Keys

A foreign key is a reference to another table. We can use those to reference a particular data item from another table!

Once datasets become larger and larger we might want to separate out data into multiple columns and sets. We can then reference these amongst each other. 

Looking at the flights data in particular, we could separate out the airports themselves into a unique table.

|id|code|city    |
|--|----|--------|
|1 |JFK |New York|   
|2 |PVG |Shanghai|
|3 |IST |Istanbul|   
|4 |LHR |London  |   
|5 |SVO |Moscow  |   
|6 |LIM |Lima    |   
|7 |CDG |Paris   |   
|8 |NRT |Tokyo   |

We can change this table and replace it with a table that has foreign keys.
It would look like this:

|id|origin_id|destination_id|duration|
|-|-|-|---|
|1|1|4|415|
|2|1|7|450|
|3|4|9|500|
|4|6|5|120| 

Once we create separate tables where we associate unique id's to individual items we can then create associated tables where we reference items from one table and associate them to another table, without hardcoding any values into them. 

### Joining Databases

SQL allows us to join multiple queries together in order to be able to see data. If we're only using unique ID's then it's difficult to see the data properly and it doesn't make things immediately obvious. 
Such a **JOIN** query could look like this
```
SELECT first, origin, destination
    FROM flights JOIN passengers
    ON passengers.flight_id = flights.id
```
SELECT tells sql what data we need
FROM tells sql what table to use
JOIN tells sql what table want to join it with (passengers in this case)
ON tells sql how the two tables are related to each other
So we're telling sql that the flight_id for each passenger is related to the flights.id
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
We can create an index of all the data which makes querying the data much easier in the long run but it requires additional memory and maintenance.
Think of an index like the index in a book. You can go to the back and look for a word and it will tell you the location of it inside of the book. 
```
CREATE INDEX name_index ON passengers (last);
```

### SQL Injection
SQL Injections are a security vulnerability where a hacker might gain access to a 
database. 

Making comments in sql is done via --. A hacker could potentially try and log in to the database and trick the system by writing a specific username containing --. This would allow you to bypass the password check.
A normal query looks like this
`SELECT * FROM users WHERE username="username" AND password = "password";`
If a hacker adds the -- lines then they might bypass the Password check and log in as the password check is effectively "commented out".
`SELECT * FROM users WHERE username="hacker" --" AND password = "";`
Everything from after the -- is effectively commented out!

Using Django allows us to write sql syntax but without having to know and understand it directly and Django also provides an extra layer of security for us by writing it for us!

#### Race Condition

A race condition is when multiple checks/threads etc are happening simultaneously. One example would that if two users were trying to see how many likes there are on particular twitter post, for example. 

To avoid these potential problems would be to add a "lock" so that when somebody is working on the database we won't allow anyone else to work on it until the initial person if finished with their work. 

## Django Models
In order for us to be able to use sql inside of Django, we need to create models. Models are classes, as referred to [here](#introduction), inside of Django that allow us to create a database. 

We need to create our database inside of `project_folder > models.py` file. 

Similar to our example regarding flights, we can now create a Flight class, that stores the origin, the destination and the duration:
```
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
```
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
```
jfk = Airport(code='JFK', city='New York)
jfk.save()
lhr = Airport(code='LHR', city='London')
lhr.save()
cdg = (Airport(code='CDG', city='Paris')
cdg.save()
nrt = Airport(code='NRT', city='Tokyo')
nrt.save()
```
Now to create a flight:
```
f = Flight(origin=jfk, destination=lhr, duration=415)
f.save()
```

This is the simplified version to create airports and flights but they important part is that we have created airports and linked them automatically to a flight via a Foreign Key. 

We can now query items from another database:
```
f.origin
# <Airport: New York (JFK)> Exactly how we have defined it in the __str__ function inside of Airport! 
f.origin.city
# 'New York'
f.origin.code
# 'JFK'
```
Because we have added the related_name argument we can also do the following:
```
lhr.arrivals.all()
<QuerySet[<Flight: 1: New York (JFK) to London (LHR)>]>
```
This will now show us all the arrivals into that particular airport!

Continue at 1:04:16
