# Program: Student Password
# Description: Demonstrates how to access a private password using name mangling.

class Student:

    def __init__(self):
        self.__password = "python123"

student = Student()
print("Student Password:",student._Student__password)