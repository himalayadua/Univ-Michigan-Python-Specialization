# Dicionaries
Collection
- once we have more than one thing inside it
- we need a way to get it back
- Lists
    - have indexes
    - 0, 1, 2, so on
    - we look them up by position
- Dictionaries
    - have key-value pairs
    - no fixed sequence
    - look up using a tag
    - most powerful data collection
    - database like operations


**Dict**
```python
# empty dictionary
expensive_cars = dict()

# add data into dict
expensive_cars['Bugatti La Voiture Noire'] = 19000000
expensive_cars['Rolls-Royce Sweptail'] = 13000000
expensive_cars['Lamborghini Veneno'] = 4500000

# print
print(expensive_cars)

```
{
    'Bugatti La Voiture Noire': 19000000,
    'Rolls-Royce Sweptail': 13000000,
    'Lamborghini Veneno': 4500000,
}



**Accessing data**
```python
expensive_cars['Lamborghini Veneno']
# 4500000

expensive_cars['Lamborghini Veneno'] = expensive_cars['Lamborghini Veneno'] + 38729

print(expensive_cars)
```
{'Bugatti La Voiture Noire': 19000000, 'Rolls-Royce Sweptail': 13000000, 'Lamborghini Veneno': `4538729`}


**Count the most common string in a list**
```python
# list of names
indian_names = ['Aarav', 'Aarav', 'Aarav', 'Ved', 'Ved', 'Aryan', 'Aryan', 'Ishaan', 'Ishaan', 'Ishaan', 'Aarav', 'Aryan']

name_counts = {}
most_common_name = None
max_count = 0

# loop through the list
for name in indian_names:

    #if name is already in dict, then increment it's counter
    if name in name_counts:
        name_counts[name] += 1
    else:
        name_counts[name] = 1
        # if name is encountered for the first time
        # then add that name as key, with 1 as value

    if name_counts[name] > max_count:
        max_count = name_counts[name]
        most_common_name = name

print("Most common Indian name:", most_common_name)
```
Most common Indian name: Aarav



**Check if a key exists**
```python
# empty dictionary
expensive_cars = dict()
expensive_cars['Bugatti La Voiture Noire'] = 19000000
expensive_cars['Rolls-Royce Sweptail'] = 13000000
expensive_cars['Lamborghini Veneno'] = 4500000

# Check if a key exists
'Lamborghini Pagani' in expensive_cars
# False
```


**GET()**
- how to check if a key exists 
- if it doesn't then don't give error
    - and return a default value
```python
indian_names = {
    'Aaradhya': 4, 'Aanya': 9, 'Aarohi': 10, 'Ananya': 5, 'Anika': 8,
    'Anaya': 7, 'Avani': 6, 'Diya': 9, 'Ishani': 3, 'Kavya': 4,
    'Kiara': 4, 'Meera': 7, 'Neha': 2, 'Pari': 3, 'Riya': 6,
    'Sara': 4, 'Shreya': 1, 'Tanvi': 5, 'Trisha': 9, 'Zara': 7
}


# look for this key
name = 'Vishakha'

# normal method
if name in indian_names:
    x = indian_names[name]
else:
    x = 0

# better method
x = indian_names.get(name, 0)
```

Using this above `get()`, let's rewrite the example above:

**Count the most common string in a list - Part2**
```python
# list of names
indian_names = [
    'Aanya', 'Aanya', 'Aarohi', 'Ananya', 'Anika', 'Anaya',
    'Anaya', 'Diya', 'Ishani', 'Kiara', 'Kiara', 'Kiara',
    'Neha', 'Neha', 'Neha', 'Sara', 'Shreya', 'Tanvi', 'Vishakha', 'Vishakha', 'Vishakha', 'Vishakha', 'Zara'
]


name_counts = {}
most_common_name = None
max_count = 0

# loop through the list
for name in indian_names:

    # if name is already in dict, then increment it's counter
    # one line
    name_counts[name] = name_counts.get(name, 0) + 1
    

    if name_counts[name] > max_count:
        max_count = name_counts[name]
        most_common_name = name

print("Most common Indian name:", most_common_name, ", with Count:", max_count)
```
Most common Indian name: Vishakha , with Count: 4




```python

```