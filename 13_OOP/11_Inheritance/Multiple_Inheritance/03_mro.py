# Program: Method Resolution Order (MRO)
# Description: Demonstrates how Python determines the order in which methods are searched in multiple inheritance.

class Father:

    def show(self):
        print("Father")

class Mother:

    def show(self):
        print("Mother")

class Child(Father, Mother):
    pass

child = Child()
child.show()
print(Child.mro())