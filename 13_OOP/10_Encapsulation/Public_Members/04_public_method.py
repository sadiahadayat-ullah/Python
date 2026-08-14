# Program: Public Method
# Description: Demonstrates how to create and call a public method to display object information.

class Car:

    def __init__(self,brand):
        self.brand = brand

    def display(self):
        print("Car Brand:", self.brand)

brand = input("Enter brand: ")

car = Car(brand)
car.display()