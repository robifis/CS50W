# Lecture 3 - Python Basics

# f strings
name = input('What is your name: ')
print(f'Hello, {name}')

# Sets
s = set() # => This will create a new set. 
s.add(value) # => This will add a value to the set.
s.remove(value) # => Removes value from set.

print(s)
# {valueOne, valueTwo}

# Dictionaries
# Creating a Dictionary
names = [
    {'name': 'Bobby'},
    {'name': 'Stacey'},
    {'name': 'Nicole'}
]
# To print a name!
print(names['name'])

# Adding a Value to the dictionary:
names['name'] = 'Nicole'

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
        
# Another example
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    # This is a new function that appends the name that we call to the list above!
    def add_passenger(self, name):
        self.passengers.append(name)

# Decorators

def announce(f):
    def wrapper():
        print('Starting the function')
        f()
        print('Function Complete')
    return wrapper

@announce
def hello():
    print('Hello, World!')

# Lambda functions

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

# Exceptions
import sys

try: 
    number1 = int(input('First Number: '))
    number2 = int(input('Second Number: '))
except: 
    print('Invalid Input')
    sys.exit(1)



