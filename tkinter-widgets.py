# self adjusting widgets:

from tkinter import *

root = Tk()

label1 = Label(root, text="first", bg="blue", fg="white")
label1.pack(fill=X)  # file upto X-axis width of the window when adjusting sides

label2 = Label(root, text="second", bg="hotpink", fg="white")
label2.pack(side=LEFT, fill=Y)      # file upto Y-axis width of the window when adjusting sides


labelone = Label(root, text="one", bg="green", fg="white")
labeltwo = Label(root, text="two", bg="black", fg="white")

labelone.pack(side=RIGHT, fill=Y)
labeltwo.pack(side=BOTTOM, fill=X)

root.mainloop()
