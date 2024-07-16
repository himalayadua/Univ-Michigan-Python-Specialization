# Regular Expressions
RegEx - study of language
- form of a language
- very old concept
- more intelligent form of search
- import regex class
    - `import re`

**re.search()**
```python
name = input("Enter file:")
handle = open(name, 'r')

# usual way
for line in handle:
    line =  line.rstrip()
    if line.find('From:') >= 0:
        print(line)

# regex way
for line in handle:
    line =  line.rstrip()
    if re.search('From:', line):
        print(line)
```
**I wouldn't use regex for something this simple**

I want to search if a line starts with `From:`
```python
# usual way
for line in handle:
    line =  line.rstrip()
    if line.startswith('From:'):    # we use a different function
        print(line)

# regex way
for line in handle:
    line =  line.rstrip()
    if re.search('^From:', line):   # same function re.search()
        print(line)
```

Regex
- ^ Start of the line
- . any char
- * 0 or more times

### Example
Read a log file and look for feature names
- i've an application
- with multiple features
- each feature is named "X-featureName"

Sample log file:
```log
X-DataPipelineAutomation: - INFO: Data pipeline completed.              #1
DataStorage - INFO: Data storage initialized.                           #2
NetworkSecurity - WARNING: Unauthorized access detected.                #3
DatabaseMaintenance - ERROR: Database connection lost.                  #4
X-NeuralNetworkOptimization: - ERROR: Neural network training failed.   #5
PerformanceMetrics - DEBUG: Measuring system performance.               #6
UserAuthentication - INFO: User logged in successfully.                 #7
X User auth pass - INFO: User logged in successfully.                   #8
X-QuantumEncryption: - INFO: Quantum encryption key generated.          #9
X-BlockchainIntegration: - INFO: Blockchain transaction confirmed.      #10
```

what regex pattern would match the rows that start with any of the feature names
`^X.*:`

This pattern will return rows: 1, 5, 8, 9, 10

If we look closely, log row 8 isn't actually a feature name, but a mismatch.
features are named "X-featureName"
```log
X User auth pass - INFO: User logged in successfully.
```
this row shouldn't be included

**Fix**
we update the regex pattern to `^X-\S+:`

Regex
- ^ Start of the line
- . any char
- * 0 or more times
- `\S match any non-white space chars`
- `+ one or more times`

This pattern `^X-\S+:` will return rows: 1, 5, 9, 10
```log
X-DataPipelineAutomation: - INFO: Data pipeline completed.              #1
X-NeuralNetworkOptimization: - ERROR: Neural network training failed.   #5
X-QuantumEncryption: - INFO: Quantum encryption key generated.          #9
X-BlockchainIntegration: - INFO: Blockchain transaction confirmed.      #10
```

### Extracting data
Let's grow our symbol database
Regex
- ^ Start of the line
- . any char
- * 0 or more times
- \S match any non-white space chars
- + one or more times
- `[] is one char`


Regex functions
- re.search()   
    - returns True/False
    - if a string matches the regex exp
- re.findall()
    - returns all matches

### Example2
**Find all numbers in a string**
Scenario: Analyzing Customer Feedback Ratings 

Suppose you work for an e-commerce company, and you receive customer feedback in the form of text reviews. Each review contains a mix of text and numeric ratings. You want to extract the numeric ratings from these reviews to analyze customer satisfaction.

Here’s an example:

Customer Review 1: “The product quality is excellent! I rate it 4 out of 5.”
```python
import re
data_string = "The product quality is excellent! I rate it 4 out of 5."
numbers = re.findall('[0-9]+', data_string)

print(numbers)
# ['4', '5']
```

### Example3
Scenario: Analyzing Text Sentiment in Customer Reviews 

Suppose you work for a product review platform, and you receive customer reviews for various products. Your task is to analyze the sentiment expressed in these reviews. Vowels often play a role in conveying emotions and intensity. Here’s how you can use the given code snippet:

You collect customer reviews like:
- “The product is amazing! I love it.”
- “Poor quality, terrible service.”

```python
import re

def extract_vowels(review):
    vowels = re.findall('[AEIOU]+', review, flags=re.IGNORECASE)
    return ''.join(vowels)

# Example reviews
review1 = "The product is amazing! I love it."
review2 = "Poor quality, terrible service."

# Extract vowels
vowels_review1 = extract_vowels(review1)
vowels_review2 = extract_vowels(review2)

print(f"Vowels in review 1: {vowels_review1}")
print(f"Vowels in review 2: {vowels_review2}")
```
Output:

Vowels in review 1: eioeIoei
Vowels in review 2: ooaeiee

Analysis:
- In review 1, the abundance of vowels suggests positive sentiment.
- In review 2, the lack of vowels (except ‘o’) indicates negative sentiment.

### Greedy matching
repeat chars
- * and +
- push outwards
- in both directions
- matches the largest possible string

**Example**
- find the section where the string starts with "From:"
- regex used '^F.+:'
    - ^F - first char is an F
    - .+ - one or more chars
    - last char is a :
- expected value 'From:'

```python
import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
```
problem:
- output: ['From: Using the :']
- expected value 'From:'

fix:
we introduce a new char
Regex
- ^ Start of the line
- . any char
- * 0 or more times
- \S match any non-white space chars
- + one or more times
- [] is one char
- `? not greedy`

```python
import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)
```
output: ['From:']


### Example4
Fetch the email address from a string

```python
import re
x = 'From Gangadhar.VMO.Shastri@gmail.com Sat Jul 15 09:30:14 2024'
y = re.findall('\S+@\S+', x)
print(y)
```
output: ['Gangadhar.VMO.Shastri@gmail.com']


**Fine Tuning String Extraction**
Parantheses:
- not part of match
- they tell where to start and stop
- what string to return after extract

```python
import re
x = 'From Gangadhar.VMO.Shastri@gmail.com Sat Jul 15 09:30:14 2024'
y = re.findall('^From (\S+@\S+)', x)
print(y)
```
output: ['Gangadhar.VMO.Shastri@gmail.com']


### Example5
**Extract domain name**
```python
x = 'From Gangadhar.VMO.Shastri@gmail.com Sat Jul 15 09:30:14 2024'
words = x.split()

email = words[1]        #   Gangadhar.VMO.Shastri@gmail.com

pieces = email.split('@')   #   ['Gangadhar.VMO.Shastri', 'gmail.com]

print(pieces[1])
```
output: 'gmail.com'


**Extract domain name using RegEx**
```python
import re
x = 'From Gangadhar.VMO.Shastri@gmail.com Sat Jul 15 09:30:14 2024'
y = re.findall('@([^ ]*)', x)

print(y)
```
output: 'gmail.com'

