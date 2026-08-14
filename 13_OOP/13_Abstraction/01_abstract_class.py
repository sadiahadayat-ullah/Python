# Program: Abstract Class

# Description: Demonstrates the use of an abstract class and
# abstract method using ABC and @abstractmethod.

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Dog barks")

dog = Dog()
dog.sound()