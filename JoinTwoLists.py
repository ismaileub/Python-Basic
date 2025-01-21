list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# using loop

myList1 = [10, 20, 30]
myList2 = ['A', 'B', 'C']

for x in myList2:
    myList1.append(x)

print(myList1)


# using extend() method

list1 = ["x", "y", "z"]
list2 = [11, 22, 33]

list1.extend(list2)
print(list1)
