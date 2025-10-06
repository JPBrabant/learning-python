# General Python syntax

## Main

Overall layout of a Python script with a main function.

```python
# First in the file.
def main():
    ...

# All the code in between.
...

# At the end of the file.
if __name__ == "__main__":
    main()
```


## If

The ternary conditional operator

```python
return "even" if n % 2 == 0 else "odd"
```

Easy way to check if a value is falsy : None, 0, empty string, False

```python
if not name:
    print('Falsy')
```

Check if a value is inside a list

```python
if house not in ['', '']:

if 'b' in 'abc':
```

Walrus operator allow you to assign and then check the result as a boolean

```python
if test := re.matches(...):
    # The results of matches is assigned to test, and if test return true (matches found something)
```


## Switch-case

The switch-case is called match in python. 

```python
match name
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: # Catch-all
        print("Who ?")
```


## For loop

```python
for i in [1,2,3]:
    print(i)
    
for i in range(3):
    print(i)
    
for _ in range(3): # If you don't care about the variable use an underscore. 
    print(something)
```


## Exception handling

```python
try:
    print("Try this line")
except ValueError:
    print("Do this if ValueError is raised")
else:
    print("Do this if no errors is raised")
```

Usefull Exceptions
- ValueError
- 


## Do nothing

You can tell a function to do nothing. It's a good way to create your
overwall layout.


```python
def function():
    ...

def function():
    pass
```


## Using modules

Importing everyting in a module force you to use the module name.

```python
import random
random.choice(["heads","tails"])
```

If you specify the exact function that you want, you don't need to use the module name.

```python
from random import choice
choice(["heads","tails"])
```

Usefull modules
- random (built-in)
- statistics (built-in) : avg, mean, ...
- sys (built-in) : quit, argv ...
- argparse (built-in) : Allow you to parse command line arguments
- requests (PyPi) : get, post
- json (PyPi) : pretty format json with json.dumps()
- pytest (PyPi) : 
- csv (built-in) : reader(), writerow(), DictReader(), DictWriter()
- re (built-in) : search (for regex)

## Packages

TODO : https://docs.python.org/3/tutorial/modules.html#packages

By adding `__init__.py` inside folder you create packages that can be imported. 


## Functions

- len(list) # Length of list  
- float(str) | int(str) | str(str) : Cast
- assert square(3) == 9
- sorted(list)
- open(file)
- input(prompt)
- type(obj)
- str.split(separator)
- str.strip()
- str.upper()
- range(n) | range(a,b,increment)
- emumarate(iterable, start=0) : Return an index and the value of iterable at index.


## Slice

```python
list = [1,2,3]
list[1:3] # Index 1 and 2 but not 3
list[1:] # Index 1 and up to the end
list[-1] # The last item
```

## Lambda

```python
lambda s: s["house"] == "Gryfindor" # A function taking a parameter called s, that return a bool.
```


### Object oriented programming

```python
class Student:
    # Static class variables
    SCHOOL = 'Hogwart'

    # Constructor
    def __init__(self, name, house):
        # Objects attributes
        self._name = name
        self._house = house
    
    # To string
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
        
    # Static method with a reference to the current class
    @classmethod
    def get(cls):
        return cls(input('name'), input('house'))

    # Static method with no reference to the current class
    @staticmethod
    def ran():
        return random.choice(range(1,10))

```


## Regex

```python
if re.search(r"^.+@.+\.edu$", email): # r = Raw string, don't interpret the backslash
re.fullmatch() # Same as search but match for begining ^ and end $ already built-in
```


## Data structures

```python
list = list()
list = []
list.append('')

tuple = (1, 2, 3) # Immutable so you can't create an empty tuple

dict = dict()
dict = {}
dict.update({'key': value})

set = set() # Only contain unique value
set.add()
```


## Type hint

Can be used with `mypy` or `pyright` of `pylance`.

```python
def test(var: int) -> str:
    var: str = ""
```


## Unpacking

Calling a function with a list and unpack the list as positional arguments

```python
print(*list)
```

Calling a function with a dictionnary, the key have to be the name of the args

```python
class.function(**kwargs)
```

You can use this to receive a variable number of args for a function that you define

```python
def function (*args, **kwargs): # The args are received as a Tuple and kwargs a Dict.
```

# Functional programming

Map

```python
uppercased = list(map(str.upper, words))
```

Filter

```python
gryfindors = list(filter(is_gryfindor, students))
gryfindors = list(filter(lambda s: s["house"] == "Gryfindor", students))
```

List comprehension

```python
uppercased = [word.upper() for word in words]
gryfindor = [{"name": student, "house": "Gryfindor"] for student in students]
```

Dict comprehension

```python
gryfindors = {student: "Gryfindor" for student in students}
```


# Generator and yield()

A for loop calling another for loop that yeild at each interation.