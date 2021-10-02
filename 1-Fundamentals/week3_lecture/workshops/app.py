from donations_pkg.homepage import show_homepage,donate, show_donations
from donations_pkg.user import login, register

database = { "admin" : "password123", "password123" : "admin", "user" : "password123"}
donations = []
authorized_user = ""

while True:
    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate")
    else:
        print(f"You are logged in as {authorized_user}")

    choice = input("Choose an option: ")
    if choice == "1":
        username = input("Enter username:").lower()
        password = input("Enter password:")
        authorized_user = login(database, username, password)
    if choice == "2":
        while True:
            username = input("Enter username:").lower()
            password = input("Enter password:")
            if len(username) > 0 and len(username) <= 10 and len(password) >= 5:
                authorized_user = register(database, username)
                database[username] = password
                break
            else:
                print("Username cannot be over 10 characters and password must be at least 5 characters.")
                continue
    if choice == "3":
        if authorized_user:
            donation, donation_sum = donate(authorized_user)
            donations.append(donation)
    if choice == "4":
        show_donations(donations)
    if choice == "5":
        exit()