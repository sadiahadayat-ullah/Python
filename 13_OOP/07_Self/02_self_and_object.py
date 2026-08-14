# Program: Self and Object
# Description: Demonstrates that 'self' and the object reference point to the same object.


class Student:

    def __init__(self):
        print(self) # Inside the constructor

student = Student()
print(student) # Outside the constructor