# Program: Age Validator
# Description: Validates age using custom exception handling.

try:
    age = int(input("Enter age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
    print("Valid age: ", age)

except ValueError as e:
    print(e)