# functional programming tells to do work using function :

def add_ten(x):
    return x + 10

def twice(func, arg):               # call any function twice
    return func(func(arg))

print(twice(add_ten, 10))
