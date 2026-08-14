# Program: Multiple Inherited Methods
# Description: Demonstrates how a child class inherits multiple methods from multiple parent classes.

class Father:

    def work(self):
        print("Father is working")
    def drive(self):
        print("Father is driving")

class Mother:

    def cook(self):
        print("Mother is cooking")
    def teach(self):
        print("Mother is teaching")

class Child(Father, Mother):
    pass

child = Child()
child.work()
child.drive()
child.cook()
child.teach()