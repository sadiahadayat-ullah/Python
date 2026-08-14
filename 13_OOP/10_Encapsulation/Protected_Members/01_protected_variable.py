# Program: Protected Variable
# Description: Demonstrates how to create and access a protected variable using an object.

class Student:

    def __init__(self):
        self._name = "Ali"

student = Student()
print("Student Name:", student._name)