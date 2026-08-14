# Program: Multiple Constructor Calls
# Description: Demonstrates that the constructor is called automatically for every object created.

class Student:

    def __init__(self):
        print("Student object created")

student1 = Student()
student2 = Student()
student3 = Student()