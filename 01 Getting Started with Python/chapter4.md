# Chapter 4
Stored Patterns:
- save some logic and give it a name
    - almost like a variable
    - holds code instead of value
- use that name anywhere else
- DRY
    - Don't Repeat Yourself


```python
def greet():
    print('Hello!')

# call the function
greet()

print('Outside function')

# call the function
greet()
```

Other functions
- print()
- max()
- int()
- float()
etc

```python
val = max("Audi")
print(val)

# u
```

### Arguments
More interactive
- pass data into a function
- variable that is used inside function code
- value of this variable
    - assigned when function is called

```python
def greet(name):
    print("Hello", name)

# pass argument
greet("Ram")
```

**Multiple Parameters**
```python
def greet(name, lang):
    if lang == "en":
        print("Hello", name)
    elif lang == "hi":
        print("Namaste", name)
    else:
        print(":)", name)

# pass argument
greet("Ram", "hi")
```

### Return value
Other things function can do
- what if we want something else
- not just print from a function
- example
    - `val = int(h)`
    - function int 
        - takes `h` as parameter
        - does something
        - doesn't print
        - return updated `h`
    - returned value is stored in variable `val`


```python
# function definition
def find_square(num):
    result = num * num
    return result

# function call
square = find_square(3)
# what ever is returned by function
# is stored in variable square

print('Square:', square)

```
