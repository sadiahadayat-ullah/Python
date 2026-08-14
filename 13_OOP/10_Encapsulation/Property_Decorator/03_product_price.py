# Program: Product Price Using @property
# Description: Demonstrates how to use the @property decorator to create a getter and setter for a private price variable with validation.

class Product:

    def __init__(self):
        self.__name = "Laptop"
        self.__price = 80000

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self.__price = new_price
        else:
            print("Price can't be negative.")

product = Product()
print("Product Name:", product.name)
print("Product Price:", product.price)

product.name = "Gaming Laptop"
product.price = 90000
print("Updated Product Name:", product.name)
print("Updated Product Price:", product.price)

product.price = -90000
print("Updated Product Price:", product.price)