# Program: Student Multilevel Inheritance
# Description: Demonstrates multilevel inheritance using Person, Student, and CollegeStudent classes.

class Person:

    def __init__(self,name):
        self.name = name

    def display_name(self):
        print("Name:",self.name)

class Student(Person):

    def __init__(self,name,roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def display_roll_no(self):
        print("Roll No:",self.roll_no)

class CollegeStudent(Student):

    def __init__(self,name,roll_no,department):
        super().__init__(name,roll_no)
        self.department = department

    def display_department(self):
        print("Department:",self.department)

name = input("Enter your name: ")
roll_no = input("Enter your roll no: ")
department = input("Enter your department: ")

college_student = CollegeStudent(name,roll_no,department)

college_student.display_name()
college_student.display_roll_no()
college_student.display_department()