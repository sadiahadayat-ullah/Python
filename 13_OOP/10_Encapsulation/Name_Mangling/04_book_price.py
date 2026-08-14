# Program: Book Price
# Description: Demonstrates how to access a private book price using name mangling.

class Book:

    def __init__(self):
        self.__price = 1500

book = Book()

print("Book Price:",book._Book__price)