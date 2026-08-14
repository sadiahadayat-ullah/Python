# Program: Arithmetic Operator Overloading
# Description: Demonstrates how dunder methods can define the behavior
# of arithmetic operators for custom objects.

class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __sub__(self, other):
        return Number(self.value - other.value)

    def __mul__(self, other):
        return Number(self.value * other.value)

    def __truediv__(self, other):
        return Number(self.value / other.value)

    def __floordiv__(self, other):
        return Number(self.value // other.value)

    def __mod__(self, other):
        return Number(self.value % other.value)

    def __pow__(self, other):
        return Number(self.value ** other.value)

num1 = Number(10)
num2 = Number(5)

print("Addition: ", (num1 + num2).value)
print("Subtraction: ", (num1 - num2).value)
print("Multiplication: ", (num1 * num2).value)
print("Division: ", (num1 / num2).value)
print("Floor Division: ", (num1 // num2).value)
print("Modulo: ", (num1 % num2).value)
print("Power: ", (num1 ** num2).value)

