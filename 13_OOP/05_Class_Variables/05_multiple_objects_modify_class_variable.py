# Program: Multiple Objects Modify Class Variable
# Description: Demonstrates that modifying a class variable through the class affects all objects.

class Student:

    school = "ABC School"

student1 = Student()
student2 = Student()
student3 = Student()

Student.school = "XYZ School"
print(student1.school)
print(student2.school)
print(student3.school)