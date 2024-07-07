# Chapter 5
Loops
- run some code again and again
- keep running something till a condition arrives


```python
languages = ['Swift', 'Python', 'Go']

# access elements of the list one by one
for i in languages:
    print(i)
```

**range() function**
Range
- returns a sequence of numbers
- `range(4)` returns a sequence of 0, 1, 2 and 3

```python
values = range(4)

# iterate from i = 0 to i = 3
for i in range(4):
    print(i)
```


### While
- `while` loop to repeat a block of code 
- until a certain condition is met
- runs the lines inside the loop
- onces all lines of code are done
- it goes back to the top
- re-checks the condition `number <= 3`

```python
number = 1

while number <= 3:
    print(number)
    number = number + 1
```


