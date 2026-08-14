# Program: Multiple Objects with Instance Variables
# Description: Demonstrates that different objects can store different instance variable values.

class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

student1 = Student("Ali",75)
student2 = Student("Sara",90)
student3 = Student("Ahmed",85)

print("Name:",student1.name,"Marks:",student1.marks)
print("Name:",student2.name,"Marks:",student2.marks)
print("Name:",student3.name,"Marks:",student3.marks)