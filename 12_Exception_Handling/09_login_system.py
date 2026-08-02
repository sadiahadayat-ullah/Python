# Program: Login System
# Description: Allows the user to log in with 3 attempts using exception handling.

correct_user = "admin"
correct_password = "python123"

for attempt in range(3):
    try:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username != correct_user or password != correct_password:
            raise ValueError("Invalid username or password")
        else:
            print("Login successful")
            break
    except ValueError as e:
        print(e)
else:
    print("Account Locked")