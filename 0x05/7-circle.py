#!/usr/bin/python3
# a module that creates a circle class with public instance attribute radius

class Circle:
    def __init__(self, radius):
        self.radius = radius # public instance attribute radius

    def calculate_area(self): # public method that returns/calculates the area of a circle
        import math
        return math.pi * (self.radius ** 2)

if __name__ == "__main__":
    circle = Circle(5)
    print(circle.calculate_area())
