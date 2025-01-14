


# Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


# Delete the entire list:

thislist = ["apple", "banana", "cherry"]
del thislist
#print(thislist)           #this will cause an error because you have succsesfully deleted "thislist".


# Clear the List
# The clear() method empties the list.

# The list still remains, but it has no content.

# Example
# Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)