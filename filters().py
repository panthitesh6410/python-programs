# to filter out particular list :

ls = [1, 3, 4, 5, 7, 9, 11, 13]

# filer(lambda exp, list) :
result = list(filter(lambda x: x % 2 == 0, ls))
print(result)

