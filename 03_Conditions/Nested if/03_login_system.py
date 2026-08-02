username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin":
    if password == "12345":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Invalid Username")