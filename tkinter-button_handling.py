from tkinter import *

root = Tk()

def action():
    print("button clicked")

button1 = Button(root, text="click!", command=action)   # command perform actions
button1.pack()

root.mainloop() 