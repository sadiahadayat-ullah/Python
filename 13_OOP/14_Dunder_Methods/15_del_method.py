# Program: __del__() Dunder Method
# Description: Demonstrates how __del__() is called when an object
# is being removed and cleaned up by Python.

class Demo:

    def __init__(self):
        print("Object created")

    def __del__(self):
        print("Object cleaned up")

demo = Demo()
del demo

