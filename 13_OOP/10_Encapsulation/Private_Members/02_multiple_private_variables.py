# Program: Multiple Private Variables
# Description: Demonstrates how to create and access multiple private variables using a public method.

class Employee:

    def __init__(self):
        self.__name = "Ali"
        self.__age = 20
        self.__salary = 1000

    def show_details(self):
        print("Employee Name:",self.__name)
        print("Employee Age:",self.__age)
        print("Employee Salary:",self.__salary)

employee = Employee()
employee.show_details()