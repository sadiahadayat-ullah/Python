# Program: Update Using Instance Method
# Description: Demonstrates how an instance method can modify an instance variable.

class Student:

    def __init__(self,name):
        self.name = name

    def display(self):
        print("Name: ", self.name)

    def update_name(self,new_name):
        self.name = new_name

student = Student("Ali")
student.display()

student.update_name("Ahmed")
student.display()