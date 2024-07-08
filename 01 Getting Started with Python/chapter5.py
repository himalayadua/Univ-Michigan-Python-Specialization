# Finding the Largest Value
# Input array
    # [9, 41, 12, 3, 74, 15]


print("Before")
# variables
largest_num = 0
counter = 0

for thing in [9, 41, 12, 3, 74, 15]:
    counter += 1
    if thing > largest_num:
        largest_num = thing
print("After")

print(largest_num)
print("Total values: ", counter)
