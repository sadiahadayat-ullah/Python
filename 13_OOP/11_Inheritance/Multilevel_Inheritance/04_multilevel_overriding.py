# Program: Multilevel Method Overriding
# Description: Demonstrates method overriding at multiple levels of inheritance.

class Animal:

    def sound(self):
        print("Animal makes a sound")

class Mammal(Animal):

    def sound(self):
        print("Mammal makes a sound")

class Dog(Mammal):

    def sound(self):
        print("Dog makes a sound")

dog = Dog()
dog.sound()