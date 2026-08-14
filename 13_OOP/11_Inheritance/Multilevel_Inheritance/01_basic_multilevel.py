# Program: Basic Multilevel Inheritance
# Description: Demonstrates how a child class inherits features through multiple levels of inheritance.

class Animal:

    def eat(self):
        print("Animal is eating")

class Mammal(Animal):

    def walk(self):
        print("Mammal is walking")

class Dog(Mammal):

    def bark(self):
        print("Dog is barking")

dog = Dog()

dog.eat()
dog.walk()
dog.bark()