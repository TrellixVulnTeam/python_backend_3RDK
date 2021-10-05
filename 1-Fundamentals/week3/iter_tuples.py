my_tuple = (1, 2, 3, 4, 5)
total = 0

print("---------------------")
for n in my_tuple:
    total += n
print(total)

print("---------------------")
for var in enumerate(my_tuple):
    print(var)

print("---------------------")
for var in my_tuple:
    print (my_tuple.index(var),var)