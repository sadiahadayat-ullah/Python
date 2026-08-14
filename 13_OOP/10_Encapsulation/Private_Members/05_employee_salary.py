# Program: Employee Salary
# Description: Demonstrates how to access a private salary using a public method.

class Employee:

    def __init__(self,name,department,salary):
        self.__name = name
        self.__department = department
        self.__salary = salary

    def show_details(self):
        print("Name:",self.__name)
        print("Department:",self.__department)
        print("Salary:",self.__salary)

name = input("Enter your name: ")
department = input("Enter your department: ")
salary = int(input("Enter your salary: "))

employee = Employee(name,department,salary)
employee.show_details()