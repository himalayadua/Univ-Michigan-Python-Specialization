# Reading Files

**file handle**
- open for reading a file
- below example `xfile` is a file handle
- python doesn't load all the data into this variable

```python
xfile = open('projectigi.txt')
for mission in xfile:
    print(mission)
```

**Count number of lines**
```python
xfile = open('projectigi.txt')
count = 0
for mission in xfile:
    count += 1

print("Total Missions:", count)
```

**Read all data into a variable**
read()
- reads the whole file
- as one long string

```python
xfile = open('projectigi-mini.txt')

data = xfile.read()
print(len(data))
# 8291
```

**Search through a file**
```python
xfile = open('projectigi.txt')
for line in xfile:
    if line.startswith('Mission:'):
        print(mission)

# Mission: 1 Trainyard

# Mission: 2 SAM Base

# Mission: 3 GOD

# ..
```
why extra empty lines:
- print adds a \n char
- one \n char already in the file at the end of each line
- fix?

```python
xfile = open('projectigi.txt')
for line in xfile:
    line = line.rstrip()
    if line.startswith('Mission:'):
        print(mission)

# Mission: 1 Trainyard
# Mission: 2 SAM Base
# Mission: 3 GOD
# ..
```

**Filename input and check file**
```python
fname = input('Enter the file name: ')

try:
    xfile = open(fname)
except:
    print("file cannot be opened: ", fname)
```
