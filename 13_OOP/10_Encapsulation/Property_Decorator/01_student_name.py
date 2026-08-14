# Program: Student Name Using @property
# Description: Demonstrates how to use the @property decorator to create a getter and setter for a private variable.

class Student:

    def __init__(self):
        self.__name = "Ali"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

student = Student()
print("Student Name:", student.name)

student.name = "Ahmed"
print("Updated Student Name:", student.name)