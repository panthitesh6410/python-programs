# make any operator do something else rather than it's original function

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

# performing operator overloading :

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

obj1 = Point(1, 4)
obj2 = Point(4, 6)

print(obj1+obj2)