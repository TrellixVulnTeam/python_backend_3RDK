class User:
    """
        Purpose: Initiate User Object
        Input: none
        Output: none
    """
    pass_list = []

    def __init__(self, name, pin, password):
        """
            Purpose: Initialize user
            Input: name, pin, password
            Output: none
        """
        self.name = name
        self.pin = pin
        self.password = self.change_password(password)
        self.pass_list = []

    def __str__(self):
        """
            Purpose: Print user information
            Input: none
            Output: string
        """
        return "Name: {}, PIN: {}, Password: {}".format(self.name, self.pin, self.password)

    def change_name(self, name):
        """
            Purpose: Change name
            Input: name
            Output: new name
        """
        self.validate_name(name)
        self.name = name
        return self.name

    def change_pin(self, pin):
        """
            Purpose: Change pin
            Input: pin
            Output: new pin
        """
        self.pin = pin
        return self.pin

    def change_password(self, password):
        """
            Purpose: Change password
            Input: password
            Output: new password
        """
        self.validate_password(password)
        self.password = password
        return self.password

    def validate_name(self, name):
        """
            Purpose: Validate name
            Input: name
            Output: boolean
        """
        if not (len(name) >=2 and len(name) <=10):
            print("Name must be between 2 and 10 characters")
            return None
        return True

    def validate_pin(self, pin):
        """
            Purpose: Validate pin
            Input: pin
            Output: boolean
        """
        if len(pin) != 4:
            print("PIN must be 4 digits")
            return None
        return True

    def validate_password(self, password):
        """
            Purpose: Validate password
            Input: password
            Output: boolean
        """
        if len(password) <= 5:
            print(f"{self.name}'s password must be greater than 5 characters")
            return None
        if ' ' in password:
            print(f"{self.name}'s password cannot have space in the string")
            return None
        if password not in self.pass_list:
            self.pass_list.append(password)
            return True
        else:
            print(f"{password} was found in the history. Please use another password")
            return None

class BankUser(User):
    """
        Purpose: Initialize Bank User
        Input: User Object
        Output: none
    """
    balance = 0
    def __init__(self, name, pin, password):
        """
            Purpose: Initialize the user object
            Input: name, pin, password
            Output: None
        """
        super().__init__(name, pin, password)
        self.on_hold = False

    def __str__(self):
        """
            Purpose: Print the user object
            Input: None
            Output: string, user object
        """
        return "Name: {}, PIN: {}, Password: {}, Balance: {}".format(self.name, self.pin, self.password, self.balance)

    def show_balance(self):
        """
            Purpose: Show the balance of the user
            Input: None
            Output: string, aoount balance
        """
        return "{:.2f}".format(self.balance)

    def deposit(self, amount):
        """
            Purpose: Deposit money to the account
            Input: amount
            Output: string, deposit amount
        """
        self.check_on_hold_status()
        if not self.amount_validation(amount):
            print("Invalid Deposit Amount")
            return None
        self.balance += amount
        return "{:.2f}".format(self.balance)

    def withdraw(self, amount):
        """
            Purpose: Withdraw money from the account
            Input: amount
            Output: string, withdraw amount
        """
        self.check_on_hold_status()
        if not self.amount_validation(amount):
            print("Invalid Withdraw Amount")
            return None
        if self.balance - amount < 0:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return "{:.2f}".format(self.balance)

    def transfer_money(self, amount, receipient):
        """
            Purpose: Transfer money to another user
            Input: amount, receipient object
            Output: boolean
        """
        self.check_on_hold_status()
        if not self.amount_validation(amount):
            print("Invalid Transfer Amount")
            return None
        if self.balance - amount < 0:
            print(f"Insufficient amount. {self.name} has {self.balance}. Transfer balance is {amount}")
            return None
        print(f"You are transferring ${amount} to {receipient.name}")
        print('Authentication required')
        new_pin = int(input("Enter your PIN: "))
        if self.pin == new_pin:
            self.balance -= amount
            receipient.balance += amount
            print("Transfer authorized")
            print(f"Transferring ${amount} to {receipient.name}")
            return True
        else:
            print("Transfer denied")
            return False

    def request_money(self, amount, sender):
        """
            Purpose: Request money from another user
            Input: amount, sender object
            Output: boolean
        """
        self.check_on_hold_status()
        if not self.amount_validation(amount):
            print("Invalid Request Amount")
            return None
        if self.balance - amount < 0:
            print(f"Insufficient amount. {self.name} has {self.balance}. Request balance is {amount}")
            return None
        print(f"You are requesting ${amount} from {sender.name}")
        print('User authentication is required...')
        new_pin = int(input(f"Enter {sender.name}'s' PIN: "))
        self_password = input("Enter your password: ")
        if sender.pin != new_pin:
            print("Invalid PIN. Transaction canceled")
            print(f"{self.name} has an account balance of: ${self.show_balance()}")
            print(f"{sender.name} has an account balance of: ${sender.show_balance()}")
            return False
        elif sender.password != self_password:
            print("Invalid Password. Transaction canceled")
            print(f"{self.name} has an account balance of: ${self.show_balance()}")
            print(f"{sender.name} has an account balance of: ${sender.show_balance()}")
            return False
        else:
            self.balance += amount
            sender.balance -= amount
            print("Request authorized")
            print(f"{sender.name} sent ${amount}")
            print(f"{self.name} has an account balance of: ${self.show_balance()}")
            print(f"{sender.name} has an account balance of: ${sender.show_balance()}")
            return True

    def amount_validation(self, amount):
        """
            Purpose: Validate the amount
            Input: amount
            Output: True or False
        """
        if amount < 0:
            return False
        return True

    def change_on_hold(self):
        """
            Purpose: Change the on_hold status of the user
            Input: None
            Output: None
        """
        if self.on_hold:
            self.on_hold = False
        else:
            self.on_hold = True

    def check_on_hold_status(self):
        """
            Purpose: Check on_hold status of the user
            Input: None
            Output: None
        """
        if self.on_hold:
            print(f"{self.name}'s transaction is rejected")
            return None
        else:
            print(f"{self.name}'s' transaction is approved")

# """ Driver Code for Task 1 """
# bob = User("Bob", "1234", "password")
# print(bob)

# """ Driver Code for Task 2 """
# bob = User("Bob", "1234", "password")
# print(bob)
# bob.change_name("Bobby")
# bob.change_pin("4321")
# bob.change_password("newpassword")
# print("-------------------")
# print(bob)

# """ Driver Code for Task 3"""
# bob = BankUser("Bob", "1234", "password")
# print(bob)

# """ Driver Code for Task 4"""
# bob = BankUser("Bob", "1234", "password")
# print(bob)
# print(bob.show_balance())
# print(bob.deposit(1000))
# print(bob.show_balance())
# print(bob.withdraw(500))
# print(bob.show_balance())

# """ Driver Code for Task 5"""
bob = BankUser("Bob", 1234, "bobpassword")
alice = BankUser("Alice", 4321, "alicepassword")

print(alice.deposit(5000))
print("Bob has $", bob.show_balance())
print("Alice has $", alice.show_balance())

print("TRANSFER MONEY")
alice.transfer_money(3000, bob)
print("Bob has $", bob.show_balance())
print("Alice has $", alice.show_balance())

print("REQUEST MONEY")
alice.request_money(500, bob)
print("Bob has $", bob.show_balance())
print("Alice has $", alice.show_balance())
