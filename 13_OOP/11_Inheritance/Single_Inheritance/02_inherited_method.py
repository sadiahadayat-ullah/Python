# Program: Inherited Method
# Description: Demonstrates how a child class can use a method inherited from its parent class.

class Animal:

    def eat(self):
        print("Animal is eating")

class Dog(Animal):

    def bark(self):
        print("Dog is barking")

dog = Dog()
dog.eat()
dog.bark()