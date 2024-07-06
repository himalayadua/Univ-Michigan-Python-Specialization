# Variables
**background**
- allocate some place in memory
- store the value in it
- create a label `v` for that memory location

```python
v = 300
```

**update**
- wait, there's already a memory space with this label
- ok, remove 300 and set 500 there
```python
v = 500
```

**Multiple variables**
```python
a = b = c = 300
print(a, b, c)
300 300 300
```

**Rules**
- Start with letter/underscore
- letters, numbers, underscore only
- Case sensitive
- Good
    - spam
    - eggs
    - spam23
    - _speed
- Bad
    - 23spam
    - #var
    - var.12
- Different variables
    - spam
    - Spam
    - SPAM
- Multi-word variable name
    - Camel Case
        - numberOfCollegeGrads
    - Pascal Case
        - NumberOfCollegeGrads
    - Snake Case
        - number_of_college_grads
- PEP 8 includes the following recommendations
    - Snake Case should be used for functions and variable names
    - Pascal Case should be used for class names




# Operators

| Operator | Operations   |
|----------|--------------|
| ^^       | Power        |
| %        | Remainder    |
| +        | Addition     |
| -        | Substraction |
| *        | Multiply     |
| /        | Division     |

Why have a separate % operator?
- pick a very large random number
- % it with 52
- now you get a number between 0 to 51
- now you can write code to randomly pick a card from a deck

**Operator Precedence**
- Highest to lowest
    - Paranthesis ()
    - Power ^^
    - Multiply, Division and Remainder
    - Addition and Substraction
- In between 2 additions
    - go Left to right


# Type

```python
print(v)
500
type(v)
<class 'int'>
```
