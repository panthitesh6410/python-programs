# used for string manipulations :

# to verify string matches a particular pattern or not

# for substitution in a string

import re

pattern = r"eggs"   # r is raw string which contains "eggs"


# match() acually compares or match two strings
if re.match(pattern, "eggszzzzzzz"):  # string should match in beginning.
    print("match found")
else:
    print("no match found")


# search()
if re.search(pattern, "zzzzeggszzzz"):      # return true when pattern found anywhere in a string
    print("match found")
else:
    print("no match found")


# findall() used to print out matched pattern
print(re.findall(pattern, "zzzzeggszzzz"))


                        # EXAMPLE PROBLEM :

string = "My name is John, John is cool"
pattern = r"John"

# replace all occuranceof john with another string :

newstring = re.sub(pattern, "Hitesh", string)
print(newstring)