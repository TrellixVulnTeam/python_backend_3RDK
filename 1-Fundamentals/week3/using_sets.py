print("---------------------")
numbers_set = {1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10}
print(numbers_set)

print("---------------------")
# numbers_set = {1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, [10, 20, 30]}
print(numbers_set)

print("---------------------")
numbers_set = {1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, (100, 200, 300)}
print(numbers_set)

print("---------------------")
words_set = {"Alpha", "Bravo", "Charlie"}
abcd = ""
for word in words_set:
    abcd += word
print(abcd)


print("---------------------")
if "Alpha" in words_set:
    print("Alpha is in set")
else:
    print("Alpha not in set")

print("---------------------")
words_set.add("Delta")
print(words_set)
words_set.discard("Bravo")
print(words_set)