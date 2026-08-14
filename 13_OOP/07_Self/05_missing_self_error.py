# Program: Missing Self Error
# Description: Demonstrates the error caused by not including self in an instance method.

class Student:

    def display():
        pass

student = Student()
student.display()