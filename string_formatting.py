# string formatting = embedd string with non-strings

numbers = [1, 2, 3]
string = "num:{0}{1}{2}".format(numbers[0], numbers[1], numbers[2])
print(string)

a = "{x}/{y}".format(x=2, y=5)
print(a)