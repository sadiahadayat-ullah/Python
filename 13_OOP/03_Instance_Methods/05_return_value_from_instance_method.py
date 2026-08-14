# Program: Return Value from Instance Method
# Description: Demonstrates how an instance method can return a value.

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_marks(self):
        return self.marks

student = Student("Ali", 75)
print("Marks: ", student.get_marks())
