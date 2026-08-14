# Program: __call__() Dunder Method
# Description: Demonstrates how __call__() allows an object to be
# called like a function.

class Multiplier:

    def __call__(self, number):
        return number * 2

multiplier = Multiplier()

print(multiplier(5))