# Program: __ne__() Dunder Method
# Description: Demonstrates how __ne__() defines the not-equal comparison
# between two custom objects using the != operator.

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __ne__(self, other):
        return self.name != other.name or self.price != other.price

pro1 = Product("Laptop", 50000)
pro2 = Product("Android", 20000)

print(pro1 != pro2)