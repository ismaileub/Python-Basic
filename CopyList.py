# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.


# Use the copy() method

import copy
firstList = [10, 30, 15, 25, 20]
secondList = firstList.copy()
print(secondList)


# Use the list() method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


# Use the slice Operator
# You can also make a copy of a list by using the : (slice) operator.

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)


#  Using List Comprehension
# List comprehension can be used to create a copy of a list, which works similarly to slicing.


original_list = [1, 2, 3, 4]
copied_list = [item for item in original_list]

print(copied_list)


# Using deepcopy() for Deep Copy
# If you want a deep copy of a list, where nested lists are also copied(not referenced), you can use deepcopy() from the copy module.

# import copy
original_list = [[1, 2], [3, 4]]
copied_list = copy.deepcopy(original_list)
copied_list[0][0] = 10
print(copied_list)  # Output: [[1, 2], [3, 4]]
