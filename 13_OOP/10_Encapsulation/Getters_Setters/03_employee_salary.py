# Program: Employee Salary Using Getter and Setter
# Description: Demonstrates how to access and modify a private salary variable using getter and setter methods with validation.

class Employee:

    def __init__(self):
        self.__name = "Ali"
        self.__department = "Finance"
        self.__salary = 10000

    def get_name(self):
        return self.__name
    def get_department(self):
        return self.__department
    def get_salary(self):
        return self.__salary

    def set_name(self,name):
        self.__name = name
    def set_department(self,department):
        self.__department = department
    def set_salary(self,salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative.")

employee = Employee()
print("Employee Name:", employee.get_name())
print("Employee Department:", employee.get_department())
print("Employee Salary:", employee.get_salary())

employee.set_salary(60000)
print("Updated Employee Salary:", employee.get_salary())

employee.set_salary(-100000)
print("Updated Employee Salary:", employee.get_salary())
