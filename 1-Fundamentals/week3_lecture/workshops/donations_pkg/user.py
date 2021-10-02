def login(database, username, password):
    if (username, password) in database.items():
        print(f"Welcome back {username}")
        return username
    elif username not in database.keys():
        print("User not found. Please register")
        return ""
    else:
        print(f"Incorrect password for {username}")
        return ""

def register(database, username):
    if username in database.keys():
        print(f"User {username} already registered")
        return ""
    else:
        print(f"User {username} registered!")
        return username