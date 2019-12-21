from tkinter import *
import tkinter.messagebox

root = Tk()


# there is a canvas to draw :

canvas = Canvas(root, width=300, height=300)
canvas.pack()

# to draw a line in canvas :

newline = canvas.create_line(0, 0, 150, 150)

otherline = canvas.create_line(10, 10, 120, 50, fill="green")

# there are more such shapes like circle, rectangles , etc...


root.mainloop()