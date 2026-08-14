# Program: Constructor Using Class Method
# Description: Demonstrates how to use a class method as an alternative constructor.

class Student:

    def __init__(self,name):
        self.name = name

    @classmethod
    def create_student(cls,name):
        return cls(name)

student = Student.create_student("Ali")
print("Name:", student.name)