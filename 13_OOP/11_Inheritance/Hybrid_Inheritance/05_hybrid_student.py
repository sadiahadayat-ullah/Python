# Program: Hybrid Student System
# Description: Demonstrates hybrid inheritance using Person, Student, Employee, and Intern classes.

class Person:

    def __init__(self,name):
        self.name = name

    def display_name(self):
        print("Name:",self.name)

class Student(Person):

    def __init__(self,name,roll_no):
        Person.__init__(self,name)
        self.roll_no = roll_no

    def display_student(self):
        print("Student Roll no:",self.roll_no)

class Employee(Person):

    def __init__(self,name,company):
        Person.__init__(self,name)
        self.company = company

    def display_employee(self):
        print("Company:",self.company)

class Intern(Student,Employee):

    def __init__(self,name,roll_no,company):
        Student.__init__(self,name,roll_no)
        Employee.__init__(self,name,company)

    def display_intern(self):
        print("Intern Information:",self.name,self.roll_no,self.company)

name = input("Enter your name: ")
roll_no = int(input("Enter your roll no: "))
company = input("Enter your company: ")

intern = Intern(name, roll_no, company)

intern.display_name()
intern.display_student()
intern.display_employee()
intern.display_intern()



