# Program: Password Validator
# Description: Validates password using custom exception handling.

try:
    password = input("Enter password: ")
    if len(password) < 8:
        raise ValueError("Password must contain at least 8 characters")
    print("Password accepted")

except ValueError as e:
    print(e)