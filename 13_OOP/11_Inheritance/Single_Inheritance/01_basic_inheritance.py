# Program: Basic Inheritance
# Description: Demonstrates how a child class inherits a method from a parent class.

class Animal:

    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    pass

dog = Dog()
dog.eat()