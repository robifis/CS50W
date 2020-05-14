- [Python](#python)
  - [Basics](#basics)
  - [Sequences](#sequences)
    - [Lists](#lists)
    - [Sets](#sets)
    - [Dictionaries](#dictionaries)
  - [Functions](#functions)
    - [Importing functions](#importing-functions)
  - [Object oriented Programming](#object-oriented-programming)
    - [Classes](#classes)
    - [Decorators](#decorators)
  - [Lambda functions](#lambda-functions)
  - [Exceptions](#exceptions)

# Python

## Basics

f string stands for formatted string.
It's a much simpler way than concatenating string.

## Sequences

- [lists]
- (tuples)
- set(sets)
- {dict}

### Lists

A list keeps items in order and have methods that can be used.

### Sets

Sets can only have unique values and do not keep things in a particular order! Values will be unique so you can't add the same item twice.
It's similar to a mathematical set => No element ever appears more than one!

To create a set we do:
`s = set()` => This will create a new set.
`s.add(value)` => This will add a value to the set.
`s.remove(value)` => Removes value from set.
This is what printing a set looks like.

```python
print(s)
# {valueOne, valueTwo}
```

### Dictionaries

```python
names = [
    {'name': 'Bobby'},
    {'name': 'Stacey'},
    {'name': 'Nicole'}
]
```

This is the structure of a dictionary.
To print the name we can access it as follows:

```python
print('name')
# 'Bobby'
```

Adding a dictionary is as follows:

```python
names['name'] = 'Nicole'
```

## Functions

```python
def square(x):
    return x * x

for i in range(10):
    print(f'The square of {i} is {square(i)}')
```

### Importing functions

**Method Nr 1 (preferred)**
If we have two different files and we want to import a function from that file we can use the import method
`from filename import functioname`
Filename is used without the .py extension and then we can use the function name to import the function.
We can then just call the function as normal

**Method Nr 2 (alternative)**
Alternatively we can just import the file as a whole:
`import filename`
However, we then need to call the function via dot notation:
`filename.functionname()` => This is how you call the function then.

## Object oriented Programming

### Classes

`self` is necessary for us to use as it references the object we're currently dealing with.

```python
# Functions
def square(x):
    return x * x

for i in range(10):
    print(f'The square of {i} is {square(i)}')

# Object Oriented Programming

class Point():
    def __init__(self, x, y):
        self.pointx = x
        self.pointy = y

# Calling it
p = Point(2,8)

# Printing the values.
print(p.pointx) # Has to match the self. side, so pointx in our case!
print(p.pointy)
```

**Another Example**

```python
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    # This is a new function that appends the name that we call to the list above!
    def add_passenger(self, name):
        self.passengers.append(name)
```

### Decorators

Decorators allow us to add additional functionality to a function.
They are handy when we want to only run functions if the user is logged in, for example.
We can therefore decorate a function to add that additional functionality.

```python
def announce(f):
    def wrapper():
        print('Starting the function')
        f()
        print('Function Complete')
    return wrapper

@announce
def hello():
    print('Hello, World!')
```

We are decorating the hello function with the announce function. The order of operation is as follows:

1. Run print Statement('Starting the function)
2. Call the function hello
3. Run the print statement at the end ('Function Complete')

The 'f' argument is the name of the function we want to call!

## Lambda functions

Lambda function works similar to Javascript where we can do one line functions, especially for functions that can be written in one simple line.

```python
people = [
    {'name': 'Bobby', 'location':'Vienna'},
    {'name': 'Nicole', 'location':'Liverpool'},
    {'name': 'Stacey', 'location':'Bulawayo'}
]

# Old way
def f(person):
    return person['name']
people.sort(key=f)

# Lambda function
people.sort(key=lambda person:person['name'])
```

It allows us to write much neater and cleaner functions!

## Exceptions

Exceptions are a good way to make our code look neater and also helps us exit a program if an error occurs.
We can use try and except including sys in order to not show the user some arbitrary error message.

```python
import sys

try:
    number1 = int(input('First Number: '))
    number2 = int(input('Second Number: '))
except:
    print('Invalid Input')
    sys.exit(1)
```
