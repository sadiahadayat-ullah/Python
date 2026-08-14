# Program: Hierarchical Method Overriding
# Description: Demonstrates how multiple child classes override the same method inherited from their parent class.

class Animal:

    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):

    def sound(self):
        print("Dog barks")

class Cat(Animal):

    def sound(self):
        print("Cat meows")

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()