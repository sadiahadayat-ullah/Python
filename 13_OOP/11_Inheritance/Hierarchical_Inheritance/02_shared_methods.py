# Program: Shared Methods
# Description: Demonstrates how multiple child classes share a method inherited from the same parent class.

class Vehicle:

    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):

    def drive(self):
        print("Car is driving")

class Bike(Vehicle):

    def ride(self):
        print("Bike is riding")

car = Car()
car.start()
car.drive()

bike = Bike()
bike.start()
bike.ride()