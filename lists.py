list1 = ["apple", "banana", "mangoes", "grapes"]

print(list1)

print(list1[1])

                # OPERATIONs ON LISTS :

list2 = [1, 1, 1, 1, 1]

# to update an element into list (at specific position):
list2[1] = 2
print(list2)

list3 = [2, 2, 2, 2, 2]

# joining two lists :
print(list2+list3)

# to print a list multiple times :
print(list2*3)

# to check that an element is present in list or not :
names = ["hitesh", "buddhi", "hari", "giri", "anuj", "rituja"]
print("anuj" in names)
print("krishna" in names)


                # LIST FUNCTIONS :

# "append()" : to append a new item to list
list1.append("Papaya")
print(list1)

# "len()" : to calculate the length of a list at end of list
print("length of list2 : ", len(list2))

# "insert()" : to insert a item at a particular position :
list1.insert(1, "orange")
print(list1)

# "index()" : return index value of an item of list :
print("position(index) of mangoes is", list1.index("mangoes"))

