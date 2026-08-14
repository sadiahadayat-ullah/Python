# Program: Student Name Using Getter and Setter
# Description: Demonstrates how to access and modify a private variable using getter and setter methods.

class Student:

    def __init__(self):
        self.__name = "Ali"

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

student = Student()
print("Student Name: ", student.get_name())

student.set_name("Ahmed")
print("Updated Student Name: ", student.get_name())