# A set is a collection which is unordered, unchangeable*, and unindexed.
# Set items are unordered, unchangeable, and do not allow duplicate values.
# Unordered means that the items in a set do not have a defined order.
thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)  # there will print apple one time


# True and 1 is considered the same value:
# False and 0 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2, False, 0}

print(thisset)
print(len(thisset))  # 6

print(type(thisset))

# It is also possible to use the set() constructor to make a set.

thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset)


################### Access Items ###################

for x in thisset:
    print(x, end=" ")

print()
# Check if "banana" is present in the set:
print("banana" in thisset)
print("banana" not in thisset)


# Converting the Set to a List
my_set = {1, 2, 3, 4, 5}

# Convert to list
my_list = list(my_set)

print(my_list[0])  # Access first element


# Add Items
Set = {10, 20, 30, 40}
Set.add("Orange")
print(Set)
