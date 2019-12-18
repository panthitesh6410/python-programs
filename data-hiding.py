class Myclass:
    # to make a variable private use "__" before the variable :
    __hiddenvariable = 0

    def add(self, increment):
        self.__hiddenvariable += increment
        print(self.__hiddenvariable)

obj1 = Myclass()
obj1.add(32)
# print(obj1.__hiddenvariable)  it cause error.

