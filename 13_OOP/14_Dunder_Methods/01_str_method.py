# Program: __str__() Dunder Method
# Description: Demonstrates how __str__() controls the user-friendly
# string representation of an object when print() is used.

class Student:

    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

    def __str__(self):
        return f"Student name: {self.name}, marks: {self.marks}"

student = Student("Ali",75)
print(student)
