from tkinter import *
import parser                   # parser to solve mathematical equations
import math

root = Tk()

root.title("calculator")

# adding input field
display = Entry(root)
display.grid(row=1, columnspan=10, sticky=W+E)       # to mak filed span from west to east

#ADDING buttons :

Button(root, text="1", command=lambda: get_variables(1)).grid(row=2,column=0)
Button(root, text="2", command=lambda: get_variables(2)).grid(row=2,column=1)
Button(root, text="3", command=lambda: get_variables(3)).grid(row=2,column=2)
Button(root, text="4", command=lambda: get_variables(4)).grid(row=3, column=0)
Button(root, text="5", command=lambda: get_variables(5)).grid(row=3, column=1)
Button(root, text="6", command=lambda: get_variables(6)).grid(row=3, column=2)
Button(root, text="7", command=lambda: get_variables(7)).grid(row=4, column=0)
Button(root, text="8", command=lambda: get_variables(8)).grid(row=4, column=1)
Button(root, text="9", command=lambda: get_variables(9)).grid(row=4, column=2)

# adding other buttons :
Button(root, text="AC", command=lambda:clear_all()).grid(row=5, column=0)
Button(root, text="0").grid(row=5, column=1)
Button(root, text="=", command=lambda: calculate()).grid(row=5, column=2)

Button(root, text="+", command=lambda: get_opertion("+")).grid(row=2, column=3)
Button(root, text="-", command=lambda: get_opertion("-")).grid(row=3, column=3)
Button(root, text="*", command=lambda: get_opertion("*")).grid(row=4, column=3)
Button(root, text="/", command=lambda: get_opertion("/")).grid(row=5, column=3)

# new operations :
Button(root, text="PI", command=lambda: get_opertion("*3.14")).grid(row=2, column=4)
Button(root, text="%", command=lambda: get_opertion("%")).grid(row=3, column=4)
Button(root, text="(", command=lambda: get_opertion("(")).grid(row=4, column=4)
Button(root, text="exp", command=lambda: get_opertion("**")).grid(row=5, column=4)

Button(root, text="<-", command=lambda: undo()).grid(row=2, column=5)
Button(root, text="!", command=lambda: fact()).grid(row=3, column=5)
Button(root, text=")", command=lambda: get_opertion(")")).grid(row=4, column=5)
Button(root, text="^2", command=lambda: get_opertion("**2")).grid(row=5, column=5)


# get user input and place it in textfield :
i=0
def get_variables(num):
   global i
   display.insert(i, num)
   i += 1               # increment index so that next integer append next to previous once


# AC and Delete button :
def clear_all():
    display.delete(0, END)

def undo():
    entire_string = display.get()
    if len(entire_string) > 0:
        new_string = entire_string[:-1]
        clear_all()         # clear entire string
        display.insert(0, new_string)
    else:
        clear_all()


# handling arithmetic operations :

def get_opertion(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

# result evaluation :
def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()        # to solve given expression
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except:
        clear_all()
        display.insert(0, "Error")

def fact(n):
    r = math.factorial(n)
    clear_all()
    display.insert(0, n)


root.mainloop()