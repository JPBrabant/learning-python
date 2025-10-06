# TODO : Add instruction to install python with uv or with the python installer.
# TODO : Learning ruff (in conjuction with pre-commit hook, or On save action in VSCode, or manually)
# TODO : Learning Pylance (language server) and Pyright (type checker built in pylance)
# TODO : Learning Polars (ML / data science ?)


# Match function
match name
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: # Catch-all
        print("Who ?")
        
        
# For loop with list
for i in [1,2,3]:
    print(i)
    
for i in range(3):
    print(i)
    
for _ in range(3): # If you don't care about the variable use an underscore. 
    print(something)
    

# Exception handling
try:
    print("Try this line")
except ValueError:
    print("Do this if ValueError is raised")
else:
    print("Do this if no errors is raised")
    
# Usefull Exception
# - ValueError
# - 
    

# Pass keyword
# The pass keyword can be using in a fuction to say that it is undefined yet
# and inside except to can't an exception but don't do anything with it. 


# Using module
# Importing everything
import random
random.choice(["heads","tails"])

# Importing a specific call.
from random import choice
choice(["heads","tails"])

# Also, if you have a file in the same directory you can import it by name.


# Usefull modules
# - random (built-in)
# - statistics (built-in) : avg, mean, ...
# - sys (built-in) : quit, argv ...
# - argparse (built-in) : Allow you to parse command line arguments
# - requests (PyPi) : get, post
# - json (PyPi) : pretty format json with json.dumps()
# - pytest (PyPi) : 
# - csv (built-in) : reader(), writerow(), DictReader(), DictWriter()
# - re (built-in) : search (for regex)
# By adding a __init__.py file inside a folder you create a module. 


# Usefull function
len(list) # Length of list  
float(str) | int(str) | str(str) # Cast
assert square(3) == 9
sorted(list)
open(file)
input(prompt)
type(obj)
str.split(separator)
str.strip()
str.upper()
range(n) || range(a,b,increment)
emumarate(iterable, start=0) # Return an index and the value of iterable at index.


# Slice
list = [1,2,3]
list[1:3] # Index 1 and 2 but not 3
list[1:] # Index 1 and up to the end
list[-1] # The last item


# Tests
# Convention : test_calculator.py and def test_square()


# Lambda
lambda student: student['name']


# Class
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    def __str__(self):
        returm self.name
        
    # Getter
    @property
    def house(self):
        return self._house
        
    # Setter
    @house.setter
    def house(self, house):
        self._house = house
        
    @classmethod
    def get(cls): # cls = current class name
        return cls(input('name'), input('house'))
        
# Static method and static attribute
class Hat
    houses = ['', '']
    
    @staticmethod # Does not have a reference to cls
    @classmethod # Have a reference to cls
    def sort(cls, name):
        print(random.choice(cls.houses))

# Interesting operator
if house not in ['', '']
if 'b' in 'abc':


# Regex
if re.search(r"^.+@.+\.edu$", email): # r = Raw string, don't interpret the backslash.
re.fullmatch() # Same as search but match for begining ^ and end $ already built-int. 


# Walrus operator, assign and check as a boolean expression
if test := re.matches(...):
    // If the matches found something, and it's assigned to the variable test.
    

# Datastructures
list = list()
list = []
list.append('')

tuple = (1, 2, 3) # Immutable so you can't create an empty tuple

dict = dict()
dict = {}
dict.update({'key': value})

set = set()
set.add()


# Type hint (mypy, pylance/pyright)
def test(var: int) -> str:
    ...


# Unpacking
# Calling a function with a list and unpack the list as positional arguments
print(*list)
# Calling with a dict, the key have to be the name of the args
class.function(**kwargs)
# A function with unlimited parameter as list or keyword
def function (*args, **kwargs): # The args are received as a Tuple and kwargs a Dict.


# Functional programming
# Map
uppercased = list(map(str.upper, words))
# Filter
gryfindors = list(filter(is_gryfindor, students))
gryfindors = list(filter(lambda s: s["house"] == "Gryfindor", students))
# List comprehension
uppercased = [word.upper() for word in words]
gryfindor = [{"name": student, "house": "Gryfindor"] for student in students]
# Dict comprehension
gryfindors = {student: "Gryfindor" for student in students}


# Generator and yield()
# A for loop calling another for loop that yeild at each interation.


# dataclasses
# Automaticaly create __init and other methods.
from dataclasses import dataclass

@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand