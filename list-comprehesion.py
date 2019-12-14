# list comprehension is defining your own rules to create a list
# list of (even squares)of numbers from 0 to 4 :

list = [x**2 for x in range(5) if x**2 % 2 == 0]
print(list)

