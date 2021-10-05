item = ("tuple item")

print(type(item))
print("---------------------")
item = ("tuple item",)

print(type(item))
print("---------------------")
item = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

print(type(item))
print("---------------------")
listA = [1, "a", True, [], 5.4]
# listB = [1; 2; 3; 4; 5]
# listC = [a, b, c, d, e]
listD = [True, False, False, True, False, True, True]
print(listA)
# print(listB)
# print(listC)
print(listD)
print("---------------------")
dictA = {"000000": "black", "ffffff": "white", "dc143c": "crimson"}
dictB = {"Geography": "Blue", "Entertainment": "Pink", "History": "Yellow", "Arts and Literature": "Purple", "Science": "Green", "Sports and Leisure": "Orange"}
dictC = {}
dictD = {5, 8, 3, 6}
print(type(dictA))
print(type(dictB))
print(type(dictC))
print(type(dictD))
print("---------------------")
my_string = "zebra"
# my_string[0] = "d"

print("---------------------")
my_string = "zebra"
print(my_string[0])
print("---------------------")
colors = {"000000": "black", "ffffff": "white", "dc143c": "crimson"}
print(colors["dc143c"])
print("---------------------")
# my_set = {1, 2, 3, 4, 5}
# print(my_set[1])

print("---------------------")

# varA = {[False, True], [True, True], [True, False], [False, False]}​
varB = {1, 1.5, 2, 2.5, 3}
varC = {4, 2, 23, 66, 23}
varD = {(1, 2), (3, 4), (5, 6)}
varE = {"alpha", "bravo", "charlie"}
varF = {}

# print(type(varA))
print(type(varB))
print(type(varC))
print(type(varD))
print(type(varE))
print(type(varF))

my_string = "Nucamp"
print(my_string[3:5])