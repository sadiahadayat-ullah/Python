# Program: Abstract Method

# Description: Demonstrates the use of an abstract method
# that must be implemented by the child class.

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car starts with a key")

car = Car()
car.start()