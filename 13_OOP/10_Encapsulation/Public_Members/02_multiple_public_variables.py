# Program: Multiple Public Variables
# Description: Demonstrates how to create and access multiple public variables using an object.

class Employee:

    def __init__(self):
        self.name = "Ali"
        self.age = 20
        self.salary = 10000

employee = Employee()
print("Employee name:", employee.name)
print("Employee age:", employee.age)
print("Employee salary:", employee.salary)