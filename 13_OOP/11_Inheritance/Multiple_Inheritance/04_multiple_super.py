# Program: Multiple Inheritance with super()
# Description: Demonstrates how super() follows the MRO in multiple inheritance.

class Father:

    def show(self):
        print("Father")

class Mother:

    def show(self):
        print("Mother")

class Child(Father, Mother):

    def show(self):
        print("Child")
        super().show()

child = Child()
child.show()