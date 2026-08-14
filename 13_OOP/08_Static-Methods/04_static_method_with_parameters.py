# Program: Static Method with Parameters
# Description: Demonstrates how a static method accepts parameters and returns a value.

class Math:

    @staticmethod
    def add(a,b):
        return a + b

print("Sum is:",Math.add(1,2))