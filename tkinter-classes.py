from tkinter import *

class MyButtons:

    def __init__(self, rootone):
        frame = Frame(rootone)
        frame.pack()

        self.printbutton = Button(frame, text="click here", command=self.printmessage)
        self.printbutton.pack()

        self.quitbutton = Button(frame, text="exit", command=frame.quit)      # frame.quit automatically quit frame (inbuilt button)
        self.quitbutton.pack(side=LEFT)

    def printmessage(self):
        print("button is clicked")

root = Tk()

b = MyButtons(root)

root.mainloop()