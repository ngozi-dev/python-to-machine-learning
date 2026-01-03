#!/usr/bin/python3
# a module that creates a class Rectangle with attributes length and width

class Rectangle:
    def __init__(self, length=0, width=0):
        self.length = length # public instance attribute length
        self.width = width   # public instance attribute width
    def area(self): # public method that returns/calculates the area of the rectangle
        return self.length * self.width
        

if __name__ == "__main__":
    rectangle = Rectangle(4, 5)
    print(rectangle.area())