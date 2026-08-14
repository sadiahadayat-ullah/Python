# Program: Multiple Objects with Instance Methods
# Description: Demonstrates that the same instance method can be used by multiple objects, each with its own data.

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name: ", self.name)
        print("Marks: ", self.marks)

student1 = Student("Ali",75)
student2 = Student("Babar",90)
student3 = Student("Rizwan",85)

student1.display()
student2.display()
student3.display()