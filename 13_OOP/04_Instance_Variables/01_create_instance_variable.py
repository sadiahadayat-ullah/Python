# Program: Create Instance Variable
# Description: Demonstrates how to create and access an instance variable using self.


class Student:

    def __init__(self,name):
        self.name = name

student = Student("Ali")
print("Student Name:",student.name)