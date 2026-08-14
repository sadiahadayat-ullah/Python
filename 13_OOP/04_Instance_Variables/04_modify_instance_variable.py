# Program: Modify Instance Variable
# Description: Demonstrates how to modify an instance variable after object creation.

class Student:

    def __init__(self,name):
        self.name = name

student = Student("Ali")
print("Name:",student.name)

student.name = "Ahmed"
print("Updated name:",student.name)

