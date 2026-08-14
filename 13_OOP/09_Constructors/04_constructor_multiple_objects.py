# Program: Constructor with Multiple Objects
# Description: Demonstrates passing different arguments to the constructor while creating multiple objects.


class Student:

    def __init__(self,name):
        print("Student Name:",name)

student1 = Student("Ali")
student2 = Student("Sara")
student3 = Student("Ahmed")
