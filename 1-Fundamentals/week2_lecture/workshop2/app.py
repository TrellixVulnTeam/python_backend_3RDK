from banking_pkg.account import *

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

print("          === Automated Teller Machine ===          ")
name = checkname()
pin = checkpin()
balance = 0
print(f"{name} has been registered with a starting balance of ${balance}")

while True:
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    user_name = input("Enter name: ")
    user_pin = input("Enter PIN: ")
    if user_name == name and user_pin == pin:
        print("Login successful!")
        break
    print("Invalid credentials")

while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        show_balance(balance)
    elif option == "2":
        balance = deposit(balance)
    elif option == "3":
        balance = withdraw(balance)
    elif option == "4":
        logout(name)
        break
    else:
        print("Invalid option")


