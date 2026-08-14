# Program: Vehicle Inheritance
# Description: Demonstrates inheritance, method overriding, and child class methods using a Vehicle and Car.

class Vehicle:

    def start(self):
        print("Vehicle is starting")

    def stop(self):
        print("Vehicle is stopping")

class Car(Vehicle):

    def drive(self):
        print("Car is driving")

    def start(self):
        print("Car is starting")

car = Car()
car.start()
car.stop()
car.drive()