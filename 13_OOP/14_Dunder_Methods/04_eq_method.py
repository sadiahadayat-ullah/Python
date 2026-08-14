# Program: __eq__() Dunder Method
# Description: Demonstrates how __eq__() defines equality comparison
# between two custom objects using the == operator.

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __eq__(self, other):
        return self.name == other.name and self.marks == other.marks

stu1 = Student("Ali", 75)
stu2 = Student("Ali", 75)

print(stu1 == stu2)