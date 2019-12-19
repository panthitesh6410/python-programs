# metacharacters :


import re

# dot '.' metacharacter :

pattern = r"a.a"        # string starts form a and ends with a and 'dot' can contain any character(s)

if re.match(pattern, "aarya"):
    print("match found")
else:
    print("no match found")


# carrot (^) and dollar ($) metacharacters :
# ^ indicates start point
# $ indicates end point

pattern1 = r"^a.i$"

if re.match(pattern1, "ashi"):
    print("match found")
else:
    print("no match found")


# star (*) metacharacter :

# it allows 0 or more repeatitions of a previous things

pattern = r"eggs(bacon)*"           # 'eggs(bacon)' can be repeated and number of times( includeing zero)

if re.match(pattern, "eggbaconbacon"):
    print("match found")
else:
    print("no match found")

# group :

pattern2 = r"bread(eggs)*bread"     # 2 breads in between any number of eggs are allowed

if re.match(pattern2, "breadeggseggseggsbread"):
    print("match found")
else:
    print("No match found")