# set data structure:
# similar as dictionary but it not allowed duplicates.

set1 = {1, 2, 3, 4, 5}
print(set1)

print(5 in set1)

# adding an element:
set1.add(6)
print(set1)

# removing an element:
set1.remove(6)
print(set1)

# UNION operation :
set2 = {10, 20, 30, 40, 50}
set3 = {100, 200, 300, 400, 500}
print(set2 | set3)

# INERSECTION operation :
print(set2 & set3)

# DIFFERENCE operation :
print(set2 - set3)

