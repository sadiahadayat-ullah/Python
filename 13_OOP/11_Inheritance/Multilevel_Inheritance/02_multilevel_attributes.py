# Program: Multilevel Attributes
# Description: Demonstrates how attributes are passed through multiple levels using multilevel inheritance and super().

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

college_student = CollegeStudent("Ali",2,"Finance")

print("Name:",college_student.name)
print("Roll no:",college_student.roll_no)
print("Department:",college_student.department)