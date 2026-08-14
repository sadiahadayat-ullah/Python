# Program: Vehicle Movement using Polymorphism

# Description: Demonstrates polymorphism by using the same move()
# method in different classes with different behaviors.

class Car:

    def move(self):
        print("Car is driving")

class Bike:

    def move(self):
        print("Bike is riding")

class Bus:

    def move(self):
        print("Bus is running")

car = Car()
bike = Bike()
bus = Bus()

for vehicle in [car, bike, bus]:
    vehicle.move()