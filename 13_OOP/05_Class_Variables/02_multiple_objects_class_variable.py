# Program: Multiple Objects with Class Variable
# Description: Demonstrates that all objects share the same class variable.

class Student:

    school = "ABC School"

student1 = Student()
student2 = Student()
student3 = Student()

print(student1.school)
print(student2.school)
print(student3.school)