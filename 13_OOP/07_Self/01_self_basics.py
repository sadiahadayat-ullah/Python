# Program: Self Introduction
# Description: Demonstrates that the 'self' keyword refers to the current object.


class Student:

    def __init__(self):
        print(self)

student = Student()