# Program: Modify Class Variable Using Class Method
# Description: Demonstrates how a class method can modify a class variable.

class Student:

    school = "ABC School"

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

student = Student()
print("School Name:",student.school)

Student.change_school("XYZ School")
print("School Name:",student.school)
