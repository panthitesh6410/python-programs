from tkinter import *

# toolbar allows to add certain tools and buttons to add , deit , create

def function1():
    print("menu item clicked")

root = Tk()

# creating main menu :
mymenu = Menu(root)     # Menu is a inbuilt class
root.config(menu=mymenu)       # to configure to window

# creating submenus :
submenu = Menu(mymenu)

# to configure and adding sub menus

mymenu.add_cascade(label="file", menu=submenu)

submenu.add_command(labe="New file", command=function1)
submenu.add_command(label="save", command=function1)

# to add a seperator:
submenu.add_separator()

submenu.add_command(label="open", command=function1)
submenu.add_command(label="exit", command=function1)

# adding new menu :
newmenu = Menu(mymenu)
mymenu.add_cascade(label="edit", menu=newmenu)
newmenu.add_command(label="edit", command=function1)
newmenu.add_command(label="undo", command=function1)
newmenu.add_command(label="share", command=function1)


# creating a toolbar :

toolbar = Frame(root, bg="hotpink")
insert_btn = Button(toolbar, text="Insert", command=function1)
insert_btn.pack(side=LEFT, padx=2, pady=3)


print_btn = Button(toolbar, text="Print", command=function1)
print_btn.pack(side=LEFT, padx=2, pady=3)

toolbar.pack(side=TOP, fill=X)

root.mainloop()

