# file object :

# f = open("e:/bootstrap/forms.html", "r")     # by default in reading moode(eithout any mode).
# print(f.name)
# print(f.mode)
# f.close()

# alter way (with context manager):
# this block of code closes file automatically 
with open("e:/bootstrap/forms.html", "r") as f:
    print(f.read())            # printing file content
    
    print(f.readline())         # prints line by line 
    # or :
    for line in f:
        print(line, end='')
        
    print(f.read(20))           # read starting 20 characters.
    
    