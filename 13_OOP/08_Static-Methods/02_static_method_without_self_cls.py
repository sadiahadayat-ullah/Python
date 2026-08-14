# Program: Static Method Without self and cls
# Description: Demonstrates that a static method does not require self or cls.

class Student:

    @staticmethod
    def show_message():
        print("This is a static method")

Student.show_message()