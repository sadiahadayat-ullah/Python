# Program: Protected Method
# Description: Demonstrates how to create and call a protected method.

class Car:

    def __init__(self,brand):
        self._brand = brand

    def _display(self):
        print("Car Brand:",self._brand)

brand = input("Enter brand: ")

car = Car(brand)
car._display()