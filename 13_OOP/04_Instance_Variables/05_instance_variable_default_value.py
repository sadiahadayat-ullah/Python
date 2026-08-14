# Program: Instance Variable with Default Value
# Description: Demonstrates how to use a default value for an instance variable through the constructor.

class Student:

    def __init__(self,name,course = "Python"):
        self.name = name
        self.course = course

student = Student("Ali")

print("Name:",student.name)
print("Course:",student.course)
