# Program: Employee Salary Using Name Mangling
# Description: Demonstrates how to access multiple private variables using name mangling.

class Employee:

    def __init__(self,name,department,salary):
        self.__name = name
        self.__department = department
        self.__salary = salary

name = input("Enter employee name: ")
department = input("Enter department: ")
salary = input("Enter salary: ")

employee = Employee(name,department,salary)

print("Employee Name:",employee._Employee__name)
print("Employee Department:",employee._Employee__department)
print("Employee Salary:",employee._Employee__salary)