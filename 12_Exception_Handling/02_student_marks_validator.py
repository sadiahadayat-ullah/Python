# Program: Student Marks Validator
# Description: Validates marks using custom exception handling.

try:
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")
    print("Valid marks:", marks)

except ValueError as e:
    print(e)