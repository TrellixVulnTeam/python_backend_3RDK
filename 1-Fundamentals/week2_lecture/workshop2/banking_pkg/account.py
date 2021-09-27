def show_balance(balance):
    print(f"Current balance: ${balance}")

def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    return balance + amount

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Where are you going to get that kind of money?")
        return balance
    else:
        return balance - amount

def logout(name):
    print(f"Goodbye {name}!")

def checkname():
    name = input("Enter name to register: ")
    while len(name) > 11 or len(name) == 0:
        if len(name) > 11:
            print("The maximum name length is 10 characters.")
        elif len(name) == 0:
            print("You must enter a name.")
        name = input("Enter name to register: ")
    return name

def checkpin():
    pin = input("Enter PIN: ")
    while len(pin) != 4:
        if len(pin) != 4:
            print("PIN must contain 4 numbers")
        pin = input("Enter PIN: ")
    return pin