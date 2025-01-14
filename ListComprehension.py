

numbers = [1, 3, 5, 7, 9]
Double = [number * 2 for number in numbers]

print(Double)


numbers = [1, 2, 3, 4, 5]

squares = []
for number in numbers:
    squares.append(number**2)

print(squares)


numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda number: number**2, numbers))

print(squares)


numbers = [1, 2, 3, 4, 5]
# And here’s the list comprehension part:
squares = [number**2 for number in numbers]

print(squares)

# syntax
#    [output_expression for element in list]


# Python list comprehension with if condition

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# newlist = [expression for item in iterable if condition == True]


# Only accept items that are not "apple":


newlist = [fruit for fruit in fruits if fruit != "apple"]
print(newlist)


# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
