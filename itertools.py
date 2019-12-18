from itertools import count, accumulate, takewhile

# count(num) counts upto infinity until we declare some terminating condition

for i in count(3):
    print(i)

    if i >= 50:
        break

# accumulate() keeps on adding one number to another number :
numbers = list(accumulate(range(0, 8)))
print(numbers)

# takewhile() take items form a list only if a certain condition remains true :


print(list(takewhile(lambda x: x <= 6, numbers)))