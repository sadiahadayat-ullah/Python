# Program: Basic Hierarchical Inheritance
# Description: Demonstrates how multiple child classes inherit from the same parent class.

class Animal:

    def eat(self):
        print("Animal is eating")

class Dog(Animal):

    def bark(self):
        print("Dog is barking")

class Cat(Animal):

    def meow(self):
        print("Cat is meowing")

dog = Dog()
dog.eat()
dog.bark()

cat = Cat()
cat.eat()
cat.meow()