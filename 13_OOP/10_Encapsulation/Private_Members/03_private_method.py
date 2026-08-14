# Program: Private Variables with User Input
# Description: Demonstrates how to store user input in private variables and display the information using a public method.

class Person:

    def __init__(self,name,city):
        self.__name = name
        self.__city = city

    def show_details(self):
        print("Name:",self.__name)
        print("City:",self.__city)

name = input("Enter your name: ")
city = input("Enter your city: ")

person = Person(name,city)
person.show_details()