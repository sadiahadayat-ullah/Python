# Program: Student Details Using Getter and Setter
# Description: Demonstrates how to access and modify multiple private variables using getter and setter methods.

class Student:

    def __init__(self):
        self.__name = "Ahmed"
        self.__age = 18
        self.__department = "Finance"

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_department(self):
        return self.__department

    def set_name(self,name):
        self.__name = name
    def set_age(self,age):
        self.__age = age
    def set_department(self,department):
        self.__department = department

student = Student()
print("Student Name:", student.get_name())
print("Student Age:", student.get_age())
print("Student Department:", student.get_department())

student.set_name("Ali")
student.set_age(20)
student.set_department("Web Technology")
print("Updated Student Name:", student.get_name())
print("Updated Student Age:", student.get_age())
print("Updated Student Department:", student.get_department())