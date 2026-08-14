# Program: Product Price Using Getter and Setter
# Description: Demonstrates how to access and modify a private product price using getter and setter methods with validation.

class Product:

    def __init__(self):
        self.__name = "Laptop"
        self.__price = 80000
        self.__quantity = 5

    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price
    def get_quantity(self):
        return self.__quantity

    def set_name(self, name):
        self.__name = name
    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            print("Price cannot be negative.")
    def set_quantity(self, quantity):
        if quantity >= 0:
            self.__quantity = quantity
        else:
            print("Quantity cannot be negative.")

product = Product()
print("Product Name:", product.get_name())
print("Product Price:", product.get_price())
print("Product Quantity:", product.get_quantity())

product.set_name("Gaming Laptop")
product.set_price(90000)
product.set_quantity(6)
print("Updated Product Name:", product.get_name())
print("Updated Product Price:", product.get_price())
print("Updated Product Quantity:", product.get_quantity())

product.set_price(-90000)
print(product.get_price())
product.set_quantity(-6)
print(product.get_quantity())