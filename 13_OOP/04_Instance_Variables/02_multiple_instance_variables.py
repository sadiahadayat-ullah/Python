# Program: Multiple Instance Variables
# Description: Demonstrates how to create and access multiple instance variables in a class.


class Student:

    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

student = Student("Ali",20,75)
print("Student Name:",student.name)
print("Student Age:",student.age)
print("Student Marks:",student.marks)