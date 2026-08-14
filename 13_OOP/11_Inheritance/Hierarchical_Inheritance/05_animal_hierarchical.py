# Program: Animal Hierarchical Inheritance
# Description: Demonstrates hierarchical inheritance using one parent class and multiple child classes.

class Animal:

    def __init__(self, name):
        self.name = name
    def eat(self):
        print("Animal is eating")

class Dog(Animal):

    def bark(self):
        print("Dog is barking")

class Cat(Animal):

    def meow(self):
        print("Cat is meowing")

class Bird(Animal):

    def fly(self):
        print("Bird is flying")

dog = Dog("Tommy")
dog.eat()
dog.bark()

cat = Cat("Kitty")
cat.eat()
cat.meow()

bird = Bird("Parrot")
bird.eat()
bird.fly()