# Program: Modify Class Variable
# Description: Demonstrates how to modify a class variable using the class name.

class Student:

    school = "ABC School"

student = Student()
print(student.school)

Student.school = "XYZ School"
print(Student.school)
print(student.school)