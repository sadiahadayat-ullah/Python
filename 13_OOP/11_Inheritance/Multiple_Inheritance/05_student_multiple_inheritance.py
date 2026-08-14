# Program: Student Multiple Inheritance
# Description: Demonstrates multiple inheritance by inheriting attributes and methods from two parent classes.

class Person:

    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)


class Course:

    def __init__(self, course_name):
        self.course_name = course_name

    def display_course(self):
        print("Course:", self.course_name)

class Student(Person, Course):

    def __init__(self, name, course_name):
        Person.__init__(self, name)
        Course.__init__(self, course_name)

    def display_student(self):
        print("Student Information:",self.name,self.course_name)

name = input("Enter your name: ")
course_name = input("Enter your course name: ")

student = Student(name, course_name)
student.display_name()
student.display_course()
student.display_student()

