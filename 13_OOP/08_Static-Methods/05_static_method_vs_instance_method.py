# Program: Static Method vs Instance Method
# Description: Demonstrates the difference between an instance method and a static method.

class Student:

    def __init__(self,name):
        self.name = name

    def display_name(self):
        print("Name:",self.name)

    @staticmethod
    def show_message():
        print("Welcome to Student Management System")

student = Student("Ali")
student.display_name()
student.show_message()