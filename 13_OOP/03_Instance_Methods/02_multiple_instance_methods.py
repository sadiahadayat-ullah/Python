# Program: Multiple Instance Methods
# Description: Demonstrates how multiple instance methods can access instance variables using the self keyword.

class Student:

    def __init__(self, name,marks):
        self.name = name
        self.marks = marks

    def display_name(self):
        print("Name:",self.name)

    def display_marks(self):
        print("Marks:",self.marks)

student = Student("Ali",75)
student.display_name()
student.display_marks()