# Lists
Collection
- more than one value in a variable

Lists
- surrounded by [ ]
- can store any element
- can be empty

```python
gameName = 'Ghost of Tsushima'

gameLevels = ['The Broken Samurai', 'The Wandering Samurai', 'The Shadow Samurai', 'The Phantom Samurai']
```

Lists
- contain items 
- that are indexed by integers
    - starting with 0

```python
# list() function
    # convert string to List
list("Samurai") 
# ['S', 'a', 'm', 'u', 'r', 'a', 'i']


# split() function
    # convert delimited string to List
games = "IGI1, IGI2, COD1" 
games_list = games.split(", ") 
games_list 
#['IGI1', 'IGI2', 'COD1']


#['IGI1', 'IGI2', 'COD1']
#   0       1       2   -- Index
# Access list elements using index
games_list[2]
# COD1


# you can also use spaces and multiple chars
# Split string on spaces 
"Think lightly of yourself and deeply of the world".split(" ")

['Think', 'lightly', 'of', 'yourself', 'and', 'deeply', 'of', 'the', 'world']



# Split string on multiple characters 
"Mississippi".split("ss") 
    
['Mi', 'i', 'ippi']

```



### Iterate over a list
Lists
- lists are iterable
- you can loop over them
    - access each element one by one
- use an `in` operator to check
    - for a string match

**You have a list of IPaddresses, check if there are any IPaddresses with 67 in them**
```python
ip_addresses = ['192.168.0.1', '10.0.0.1', '67.123.45.68', '172.16.0.1', '67.89.67.123']

for ip_address in ip_addresses:
    if '67' in ip_address:
        print(f"IP address {ip_address} contains '67'")
```
IP address 67.123.45.67 contains '67'
IP address 67.89.67.123 contains '67'


**What if I only want IPaddresses where 67 occurs twice**
```python
ip_addresses = ['192.168.0.1', '10.0.0.1', '67.123.45.68', '172.16.0.1', '67.89.67.123']

for ip_address in ip_addresses:
    if ip_address.count('67') == 2:
        print(f"IP address {ip_address} contains '67' twice")
```
IP address 67.89.67.123 contains '67' twice

**count()** method:
- used to count the occurrences


### Update a list

```python
cod_games = ['CoD', 'CoD 2', 'CoD 4: Modern Warfare', 'CoD 4: Modern Warfare', 'CoD: World at War', 'CoD: Ghosts', 'CoD: Advanced Warfare']

# seems like we made a mistake
# 'CoD 4: Modern Warfare' is repeated twice
cod_games[3] = 'CoD 4: Modern Warfare 2'

    
['CoD', 'CoD 2', 'CoD 4: Modern Warfare', 'CoD 4: Modern Warfare 2', 'CoD: World at War', 'CoD: Ghosts', 'CoD: Advanced Warfare']
# looks better
```

**Update a list using a slice**
- i want to update first 2 items
- and i want to update that in a single step
```python
cod_games = ['CoD', 'CoD 2', 'CoD 4: Modern Warfare', 'CoD 4: Modern Warfare', 'CoD: World at War', 'CoD: Ghosts', 'CoD: Advanced Warfare']

# ['CoD', 'CoD 2', 'CoD 4: Modern Warfare', ...
#   0       1          2        --indexes
cod_games[0:2] = ['Call of Duty', 'Call of Duty 2']
```
['Call of Duty', 'Call of Duty 2', 'CoD 4: Modern Warfare', 'CoD 4: Modern Warfare', 'CoD: World at War', 'CoD: Ghosts', 'CoD: Advanced Warfare']

Why [0:2] and not [0:1]?
- remember in slicing, the last value is not included
- [0:2] means 0 and 1

