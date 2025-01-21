# Tuple items are ordered, unchangeable, and allow duplicate values.

thisTuple = ("Rose", "Cherry", "Lily")
print(thisTuple)

print(len(thisTuple))

# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

name = ("Ismail",)
print(name)
print(type(name))


# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.

# note the double round-brackets
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

# Access Tuple Items
print(thistuple[0])
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print(thistuple[:4])       # 0 to 3
print(thistuple[2:])       # 2 to end

if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

# Update Tuples
# Add Items
# Add tuple to a tuple using ternary(+) operator
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)


# delete tuple
del thisTuple


for x in thistuple:
    print(x)

for x in thistuple:
    print(x, end=" ")

print()

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)
