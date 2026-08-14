# Program: Object vs Class Variable
# Description: Demonstrates that assigning to an object creates an instance variable that hides the class variable for that object.

class Student:

    school = "ABC School"

student = Student()
print(student.school)

student.school = "XYZ School"
print(student.school)
print(Student.school)