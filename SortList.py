# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

numberList = [100, 50, 65, 82, 23]
numberList.sort()
print(numberList)


# Sort Descending

thislist.sort(reverse=True)
print(thislist)

numberList.sort(reverse=True)
print(numberList)


# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

# Case sensitive sorting can give an unexpected result:

# here orange and kiwi start with capital letter
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)


# so made caseInsensitive by using str.lower
# Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)


# *************************************************************#
# To sort a list without modifying the original list, you can use the sorted() function in Python. It creates and returns a new sorted list, leaving the original list unchanged.

# Original list
my_list = [5, 3, 8, 1, 2]

# Create a sorted version of the list
sorted_list = sorted(my_list)

# Print the sorted list and the original list
print("Original List:", my_list)
print("Sorted List:", sorted_list)

# Sorting in Descending Order:
desc_sorted_list = sorted(my_list, reverse=True)
print("Descending Sorted List:", desc_sorted_list)
print("Original List:", my_list)


# Sorting with a Custom Key:
# For example, sort by string length:

words = ["apple", "kiwi", "banana", "cherry"]
sorted_by_length = sorted(words, key=len)
print("Sorted by Length:", sorted_by_length)

# Sorting based on absolute values
# List of numbers
numbers = [-7, -3, 8, 4, -5]

# Sort by absolute value in ascending order
sorted_numbers = sorted(numbers, key=abs)
print(sorted_numbers)  # Output: [-3, -5, 4, 8, -7]
