# Program: Protected Variables with User Input
# Description: Demonstrates how to store user input in protected variables and display the information.

class Person:

    def __init__(self,name,city):
        self._name = name
        self._city = city

name = input("Enter your name: ")
city = input("Enter your city: ")

person = Person(name,city)

print("Name:",person._name)
print("City:",person._city)


