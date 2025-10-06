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

Usefull Exception
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

