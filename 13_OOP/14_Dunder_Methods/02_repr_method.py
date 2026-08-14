# Program: __repr__() Dunder Method
# Description: Demonstrates how __repr__() provides a developer-friendly
# representation of an object for debugging and inspection.

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(name = '{self.name}', price = {self.price})"

product = Product("Laptop", 50000)
print(product)


