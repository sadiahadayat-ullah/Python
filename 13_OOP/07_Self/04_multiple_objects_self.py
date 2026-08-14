# Program: Multiple Objects with self
# Description: Demonstrates that the 'self' keyword refers to the object that calls the instance method.


class Student:

    def display(self):
        print(self)

student1 = Student()
student2 = Student()
student3 = Student()

student1.display()
student2.display()
student3.display()