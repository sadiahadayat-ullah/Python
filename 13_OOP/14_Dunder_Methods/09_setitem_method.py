# Program: __setitem__() Dunder Method
# Description: Demonstrates how __setitem__() allows a custom object
# to modify items using the square bracket [] operator.

class ShoppingCart:

    def __init__(self, items):
        self.items = items

    def __setitem__(self, index, value):
        self.items[index] = value

cart = ShoppingCart(["Book", "Pen", "Bag"])
cart[1] ="Laptop"

print(cart.items)
