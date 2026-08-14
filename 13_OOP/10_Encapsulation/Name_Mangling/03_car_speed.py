# Program: Car Speed
# Description: Demonstrates how to access a private speed using name mangling.

class Car:

    def __init__(self):
        self.__speed = 100

car = Car()

print("Car speed:",car._Car__speed)