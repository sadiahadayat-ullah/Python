# Program: Multiple Protected Variables
# Description: Demonstrates how to create and access multiple protected variables using an object.

class Employee:

    def __init__(self):
        self._name = "Ali"
        self._age = 20
        self._salary = 10000

employee = Employee()
print("Employee Name:", employee._name)
print("Employee Age:", employee._age)
print("Employee Salary:", employee._salary)