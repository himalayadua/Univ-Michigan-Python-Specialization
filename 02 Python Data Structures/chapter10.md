# Tuples
What are they:
- are like lists
- `can't be modified`
- indexed from 0

```python
#lists
x = [9, 8, 7]
x[2] = 6
print(x)
# [9, 8, 6]

#strings
v = "apple"
v[2] = l
# Error
# Traceback: 'str' does not support assignment

#tuples
t = (9, 8, 7)
t[2] = 6
# Error
# Traceback: 'tuple' does not support assignment
```

### Other things `not supported`
Tuple:
- sort()
- append()
- reverse()

Available functions in List vs Tuple
![Available Functions](./assets/tuple-limitation.png)


### Advantages
More Efficient
- simpler
- more efficient in terms of memory use and performance

Using tuple to assign multiple variables
```python
(x, y) = (44, 99)

print(y)
# 99
```

Tuples are comparable
- if first item is same
    - then it goes to next element
```python
(0, 1, 2) < (5, 1, 2)
# True
```

**Sorted()**
```python
c = {'a':10,'b':1,'c':22}
tmp = list()

for k, v in c.items():
    tmp.append((v, k))

print(tmp)
# [(10, 'a'), (1, 'b'), (22, 'c')]

tmp = sorted(tmp, reverse=True)
print(tmp)
# [(22, 'c'), (10, 'a'), (1, 'b')]
```


```python

```


```python

```
