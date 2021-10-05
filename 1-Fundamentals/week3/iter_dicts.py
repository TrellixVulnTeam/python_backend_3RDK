state_capitals = {"Washington": "Olympia", "Oregon": "Salem", "California": "Sacramento"}
for state in state_capitals:
    print(state)


print("---------------------")
for city in state_capitals.values():
    print(city)

print("---------------------")
for state in state_capitals:
    print(state_capitals[state], "is the capital of", state)

print("---------------------")
for state, city in state_capitals.items():
    print(city, "is the capital of", state)