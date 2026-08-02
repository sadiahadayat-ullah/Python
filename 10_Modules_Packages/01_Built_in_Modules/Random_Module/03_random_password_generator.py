import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

length = int(input("Enter the length of the password: "))
if length <= 0:
    print("Password must be greater than 0")
else:
    password = ""
for i in range(length):
    password += random.choice(characters)
print(f"Your password is: {password}")