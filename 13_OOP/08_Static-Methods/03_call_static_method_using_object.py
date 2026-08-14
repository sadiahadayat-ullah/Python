# Program: Call Static Method Using Object
# Description: Demonstrates that a static method can be called using an object.

class Student:

    @staticmethod
    def greet():
        print("Hello Students!")

student = Student()
student.greet()