# Program: Self in Instance Method
# Description: Demonstrates that the 'self' keyword refers to the object that calls an instance method.

class Student:

    def display(self):
        print(self)

student = Student()
student.display()