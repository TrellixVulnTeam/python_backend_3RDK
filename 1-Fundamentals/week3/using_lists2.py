states = ["Washington", "Oregon", "California", "New York", "Oregon", "Washington", "North Carolina", "Florida"]
states2 = ["Arizona", "Ohio", "Louisiana"]

print("\n")
for x in states:
    print(x)

print("\n")
for state in states:
    print(state)

print("\n")
for state in states:
    state = state.lower()
    print(state)

print("\n")
print("Washington" in states)
print("Tennessee" in states)
print("Washington" not in states)


print("\n")
best_states = states + states2
print(best_states)

print(best_states[1:3])
print(best_states[:2])
print(best_states[4:])
print(best_states)
best_states.pop(0)
print(best_states)

my_mult_list = [[1,2,3], [4,5,6], [7,8,9]]
print(my_mult_list[-1][-1])