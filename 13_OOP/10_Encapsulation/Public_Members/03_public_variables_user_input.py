# Program: Public Variables with User Input
# Description: Demonstrates how to store user input in public variables and display the information.

class Person:

    def __init__(self,name,city):
        self.name = name
        self.city = city

name = input("Enter your name: ")
city = input("Enter your city: ")

person = Person(name,city)

print("Name:", person.name)
print("City:", person.city)