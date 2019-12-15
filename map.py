# map : allows opeartions on a list :

def add(x):
    print(x**2)

l = [1, 2, 3, 4, 5]

# map() :
result = list(map(add, l))
print(result)

  