# dictionary - <key, value> pairs :

age = {"John": 19, "Rob": 23}
print(age["John"])      # printing value of key

                        # Dictionary Functions :

num = {1: "one", 2: "two", 3: "three", 4: "four"}

# check if a value is resent in dict or not
print(4 in num)         # if present it returns true, else false

# to retrieve value of a particular key
print(num.get(3))           # it prints value corresponds to specified kay
# if a value not found then:
print(num.get(5, "not found"))

