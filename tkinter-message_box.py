from tkinter import *
import tkinter.messagebox

root = Tk()


# type - 1: showinfo()
tkinter.messagebox.showinfo("title", "this is good")    # creating a popup with text as "this is good"


#type - 2: askquestion()
response = tkinter.messagebox.askquestion("Question1", "do you like tea")
if response == "yes":
    print("Go to hell")
else:
    print("very good")




root.mainloop()