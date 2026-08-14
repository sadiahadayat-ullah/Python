#Program: Inherited Attributes
# Description: Demonstrates how a child class can inherit an attribute from its parent class.

class Animal:

    def __init__(self,name):
        self.name = name

class Dog(Animal):
    pass

dog = Dog("Tommy")
print("Dog Name:",dog.name)
