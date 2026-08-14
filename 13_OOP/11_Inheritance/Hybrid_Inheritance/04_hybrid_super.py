# Program: Hybrid Inheritance with super()
# Description: Demonstrates how super() follows the MRO through a hybrid inheritance structure.

class Person:

    def show(self):
        print("Person")

class Student(Person):

    def show(self):
        print("Student")
        super().show()

class Employee(Person):

    def show(self):
        print("Employee")
        super().show()

class Intern(Student, Employee):

    def show(self):
        print("Intern")
        super().show()

intern = Intern()
intern.show()
