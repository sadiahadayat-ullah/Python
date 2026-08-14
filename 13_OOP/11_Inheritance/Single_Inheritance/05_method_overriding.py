# Program: Method Overriding
# Description: Demonstrates how a child class can override a method of its parent class.

class Animal:

    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):

    def sound(self):
        print("Dog barks")

dog = Dog()
dog.sound()