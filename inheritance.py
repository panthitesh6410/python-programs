 # creating class :

class Students:

 # to define attributes and properties of a class, we use init function.

     # DEFINING ATTRIBUTES :

     def __init__(self, name, contact):
         self.name = name
         self.contact = contact

     # METHODS :

     def getdata(self):
         print("accepting data")
         self.name = input("enter name : ")
         self.contact = input("enter contact : ")

     def putdata(self):
         print("printing data")
         print("name is "+self.name)
         print("contact is " + self.contact)

# inheritance syntax :

class ScienceStudent(Students):

    def __init__(self, age):
        self.age = age

    def science(self):
        print("i am a science student")

john = ScienceStudent(20)
john.science()
john.getdata()
john.putdata()