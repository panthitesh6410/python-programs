from itertools import count
from itertools import accumulate

# count(num) counts upto infinity until we declare some terminating condition

for i in count(3):
    print(i)

    if i >=50:
        break

# accumulate() keeps on adding one number to another number :