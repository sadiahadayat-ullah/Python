# Program: Shape Area using Polymorphism
import math

# Description: Demonstrates polymorphism by using the same area()
# method in different classes with different calculations.

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):

        area = self.radius * self.radius * math.pi
        print("Circle area is:", area)

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print("Rectangle area is:", area)

class Square:

    def __init__(self, side):
        self.side = side

    def area(self):
        area = self.side * self.side
        print("Square area is:", area)

circle = Circle(5)
rectangle = Rectangle(10, 5)
square = Square(4)

for shape in [circle, rectangle, square]:
    shape.area()