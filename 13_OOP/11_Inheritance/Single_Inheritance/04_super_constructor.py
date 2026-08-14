# Program: super() Constructor
# Description: Demonstrates how super() is used to call the parent class constructor.

class Person:

    def __init__(self,name):
        self.name = name

class Student(Person):

    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

name = input("Enter your name: ")
age = input("Enter your age: ")

student = Student(name,age)

print("Student Name:",student.name)
print("Student Age:",student.age)