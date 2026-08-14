# Program: Student Inheritance
# Description: Demonstrates inheritance, super(), constructors, attributes, and methods using Person and Student classes.

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:",self.name)
        print("Age:",self.age)

class Student(Person):

    def __init__(self, name, age,roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def display_student(self):
        print("Student Roll No:",self.roll_no)

name = input("Enter your name: ")
age = input("Enter your age: ")
roll_no = input("Enter your roll no: ")

student = Student(name,age,roll_no)

person = Person(name,age)

student.display_person()
student.display_student()