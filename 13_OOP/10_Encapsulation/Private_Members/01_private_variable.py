# Program: Private Variable
# Description: Demonstrates how to create and access a private variable using a public method.

class Student:

    def __init__(self):
        self.__name = "Ali"

    def show_name(self):
        print("Name:",self.__name)

student = Student()
student.show_name()