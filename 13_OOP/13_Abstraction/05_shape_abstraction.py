# Program: Shape Abstraction
import math
# Description: Demonstrates abstraction using an abstract Shape
# class with different implementations of the area() method.

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = self.radius * self.radius * math.pi
        print("Circle area: ", area)

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print("Rectangle area: ", area)

circle = Circle(5)
circle.area()

rectangle = Rectangle(10, 5)
rectangle.area()
