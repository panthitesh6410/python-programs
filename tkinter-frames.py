from tkinter import *

# frame is a container which will hold widgets in a window :

root = Tk()     # mandatory

# creating a frame :
newframe = Frame(root)
newframe.pack()

otherframe = Frame(root)
otherframe.pack(side="bottom")

# creating buttons
button1 = Button(newframe, text="click me", fg="lightblue")     # creating a button on newframe
button2 = Button(otherframe, text="click me", fg="hotpink")   # creating a button on otherframe

# to add buttons on layout :
button1.pack()
button2.pack()

root.mainloop()         # mandatory

