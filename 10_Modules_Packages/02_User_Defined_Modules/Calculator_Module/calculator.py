"""
This module provides basic calculator functions.
"""
def add(a,b):
    """ returns the sum of two numbers """
    return a+b
def subtract(a,b):
    """ returns the subtraction of two numbers """
    return a-b
def multiply(a,b):
    """ returns the product of two numbers """
    return a*b
def divide(a,b):
    """ returns the quotient of two numbers """
    return a/b

PI = 3.1415926
Author = "Ali"

if __name__ == "__main__":
    print("Calculator module is running directly ")
    print(add(10,20))