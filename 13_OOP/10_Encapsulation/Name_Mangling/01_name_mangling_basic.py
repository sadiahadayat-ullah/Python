# Program: Basic Name Mangling
# Description: Demonstrates how to access a private variable using name mangling.

class Student:

    def __init__(self):
        self.__name = "Ali"

student = Student()
print("Student Name:",student._Student__name)