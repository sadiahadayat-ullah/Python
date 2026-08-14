# Program: Public Variable
# Description: Demonstrates how to create and access a public variable using an object.

class Student:

    def __init__(self):
        self.name = "Ali"

student = Student()
print("Name:", student.name)