# Program: Multilevel super()
# Description: Demonstrates how super() calls constructors through multiple levels of inheritance.

class Person:

    def __init__(self,name):
        self.name = name

class Student(Person):

    def __init__(self,name,roll_no):
        super().__init__(name)
        self.roll_no = roll_no

class CollegeStudent(Student):

    def __init__(self,name,roll_no,department):
        super().__init__(name,roll_no)
        self.department = department

name = input("Enter your name: ")
roll_no = input("Enter your roll no: ")
department = input("Enter your department: ")

college_student = CollegeStudent(name,roll_no,department)

print("Name:",college_student.name)
print("Roll no:",college_student.roll_no)
print("Department:",college_student.department)