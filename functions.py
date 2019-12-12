# defining a function :
def fun():
    print("this is a function")
    print("function can be called any number of times")
    print("functions allow for code reusability")
fun()


# function having arguments and returning no value :
def add(a, b):
    print("addition of", a, "and", b, "is", a+b)
add(5, 4)
add(123, 100)


# function having arguments and returning something :
def addition(x, y):
    c = x + y
    return c
result = addition(32, 45)
print("addition result is :", result)


# passing function as an argument to another function :
def sq(num):
    return num*num
square = sq(addition(2, 3))
print(square)

