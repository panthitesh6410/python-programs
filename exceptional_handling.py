try:                    # contains code that may contain an exception
    a = 20
    b = 0
    print(a / b)
except ZeroDivisionError:           # handling occurred exception
    print("there is a divide by zero error")
finally:
    print("This is gonna be executed any how")