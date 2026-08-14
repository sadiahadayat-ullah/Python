# Program: Call Class Method Using Object
# Description: Demonstrates that a class method can be called using an object.

class Student:

    school = "ABC School"

    @classmethod
    def display_school(cls):
        print("School Name:", cls.school)

student = Student()
student.display_school()