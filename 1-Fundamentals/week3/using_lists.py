states = ["Washington", "Oregon", "California"]
print('-------')
print(states[0])
print(states[1])
print(states[2])

print('-------')
print(states[-1])
print(states[-2])
print(states[-3])

print('-------')
states[2] = "Arizona"
print(states)

print('-------')
print(len(states))

print('-------')
states.append("New York")
print(states)

print('-------')
states.pop(1)
print(states)

print('-------')
states.pop()
print(states)