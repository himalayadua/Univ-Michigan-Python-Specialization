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

**Common Practice**
- we name variables that mean something
- the complete set of languges is named `languages`
- the variable that gets language one at a time
    - is named `language`
- this is for our understanding only
- python doesn't care if you reverse this above logic

```python
languages = ['Swift', 'Python', 'Go']

# access elements of the list one by one
for language in languages:
    print(language)
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


**Definite Loop**
Fixed set
- run something 5 times

```python
values = [5, 4, 3, 2, 1]

for i in values:
    print(i)
```

**What is IN**
for i in values
- member of
- loop will run multiple times
    - equal to number of elements in `values`
- each value, one at a time, will be stored in `i` variable
- this logic is dictated by `in` operator


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

### Break out
Break
- ends current loop
- jumps to statement immediately after the loop
- gets us out of the loop

```python
# infinite loop
while True:
    line = input("> ")  #keep prompting for inputs
    if line == 'done':  #the program stops, only when user enters done
        break
    print(line)
print("Done!")
```

### Continue = skip
Continue
- ends the current step of loop
- ends the current iteration
- jumps to top of the loop
- starts next iteration
- `doesn't` gets us out of the loop

```python
# infinite loop
while True:
    line = input("> ")  #keep prompting for inputs

    if line[0] == '#':  #if user enters # as the first char of input
        continue        #code skips everything after this line

    if line == 'done':  #the program stops, only when user enters done
        break
    print(line)
print("Done!")
```


### Counting inside loop
Simple
- create a counter variable
- set to = 0
- increment it inside the loop

Enumerate
- function adds a counter to an iterable

```python
shopping = ['cruise', 'helicopter', 'ferrari']

for item in shopping:
  print(item)


# Output
#cruise
#helicopter
#ferrari


# loop over an enumerate object
for count, item in enumerate(grocery):
  print(count, item)

# Output
#0  cruise
#1  helicopter
#2  ferrari

```

**enumerate() Syntax**

```python
enumerate(iterable, start=0)
```


**Skip a value**
Next()
- access the next element from an enumerated sequence

```python
shopping = ['cruise', 'helicopter', 'ferrari']

enumerateShopping = enumerate(shopping)

# accessing the next element
next_element = next(enumerateShopping)

print(f"Next Element: {next_element}")
```

