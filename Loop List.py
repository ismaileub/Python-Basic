
from itertools import count

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x, end=" ")  # Items will be printed in a single line separated by spaces

print()
# Use the range() and len() functions to create a suitable iterable.


for i in range(len(thislist)):
    print(thislist[i])


for i in range(0, 3):
    print(i)


# Print all items, using a while loop to go through all the index numbers

secondList = [10, 20, 30, 40]
i = 0
while i < len(secondList):
    print(secondList[i])
    i += 1


for i in count(start=0):  # `itertools.count` generates numbers indefinitely
    print(i)
