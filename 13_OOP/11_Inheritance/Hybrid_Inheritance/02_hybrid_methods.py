# Program: Hybrid Inheritance with Methods
# Description: Demonstrates how a class can inherit methods through a hybrid inheritance structure.

class Person:

    def display_person(self):
        print("Person")

class Student(Person):

    def study(self):
        print("Student is studying")

class Employee(Person):

    def work(self):
        print("Employee is working")

class Intern(Student, Employee):

    def train(self):
        print("Intern is training")

intern = Intern()
intern.display_person()
intern.study()
intern.work()
intern.train()