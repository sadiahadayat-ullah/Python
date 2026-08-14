# Program: Student Age Using @property
# Description: Demonstrates how to use the @property decorator to create a getter and setter for a private variable with validation.

class Student:

    def __init__(self):
        self.__age = 18

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age >= 0:
            self.__age = new_age
        else:
            print("Age can't be negative.")

student = Student()
print("Student Age:", student.age)

student.age = 20
print("Student Age:", student.age)

student.age = -5
print("Student Age:", student.age)