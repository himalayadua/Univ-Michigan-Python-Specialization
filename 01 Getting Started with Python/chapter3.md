# Chapter 3
Conditional steps:
- asking a question
- can be True or False
- statements based on this question
    - are indented
    - notice the <statement> below

```python
if <expr>:
    <statement>

# All the statements are executed only IF is TRUE
if <expr>:
    <statement>
    <statement>
    ...
    <statement>
<following_statement>
```



**How it's actually used**
```python
if line contains "Error": 
      errors += 1
```

**Give the code 2 pathways**
Two-way decisions
```python
if result == 'Success':
    success += 1
else:
    failed += 1
```

Example:
```python
car = 'Ferrari'

if car == "Ferrari": 
      print("Buy it")

quantity = 5

if quantity > 4:
    print("Greater than 4")

if quantity != 6:
    print("Not equal to 6")

```


### Multiple Conditions
Elif
- combination of Else and If
- if one elif is executed
    - it skips all rest of the elif after that

```python
if <expr>:
    <statement(s)>
elif <expr>:
    <statement(s)>
elif <expr>:
    <statement(s)>
    ...
else:
    <statement(s)>
```

Can be done in a single line per condition:
```python
quantity = 2
if quantity == 1: print('one'); print('two'); print('three')
elif x == 2: print('Buy 2'); print('Car')
else: print('No Cars'); print('to buy')

# Output
#Buy 2
#Car
```


### Ternary Operator
Conditional Expression
- not a control structure that directs the flow of program execution
- acts more like an operator
- Example below
    - <conditional_expr> is evaluated first
    - if it is true, the expression evaluates to <expr1>
    - if it is false, the expression evaluates to <expr2>

```python
<expr1> if <conditional_expr> else <expr2>
```

```python
debugging = False
print("The program will print", 'no errors' if not raining else 'all errors')

# The program will print no errors
```


Calculate the max of 2 numbers:
```python
m = a if a > b else b
```


