username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin" and password == "":
    print("Login Successful")
elif username != "admin":
    print("Invalid Username")
else:
    print("Invalid Password")