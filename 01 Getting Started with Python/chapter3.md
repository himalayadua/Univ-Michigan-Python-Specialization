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

Give the code 2 pathways:
```python
if result == 'Success':
    success += 1
else:
    failed += 1
```

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