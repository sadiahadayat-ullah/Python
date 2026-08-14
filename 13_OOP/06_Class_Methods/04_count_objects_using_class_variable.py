# Program: Count Objects Using Class Variable
# Description: Demonstrates how to count the number of objects using a class variable and a class method.

class Student:

    count = 0

    def __init__(self):
        Student.count += 1

    @classmethod
    def display_count(cls):
        print("Total objects:", cls.count)

student1 = Student()
student2 = Student()
student3 = Student()

Student.display_count()