username = input("Enter your username: ")
password = input("Enter your password: ")

with open("login.txt","a") as f: # append
    f.write(f"Username: {username}\n")
    f.write(f"Password: {password}\n")
    f.write("\n")

print("Login details saved successfully")