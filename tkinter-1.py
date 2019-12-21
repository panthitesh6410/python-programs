from tkinter import *

# creating a window :
root = Tk()
# Tk() is class from tkinter package and object is root

# creating a label :
label1 = Label(root, text="hello world")

# adding label to window :
label1.pack()           #it packs label on window

root.mainloop()         # it helps to make window stay.

