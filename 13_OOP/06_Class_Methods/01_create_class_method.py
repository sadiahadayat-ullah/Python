# Program: Create Class Method
# Description: Demonstrates how to create a class method and access a class variable using cls.

class Student:

    school = "ABC School"

    @classmethod
    def display_name(cls):
        print("School Name:", cls.school)

Student.display_name()