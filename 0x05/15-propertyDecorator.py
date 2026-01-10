#!/usr/bin/python3
# a module that creates a class Rectangle with 
# private attributes __length and __width

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    
    @property # getter method for length
    def length(self):
        """Getter for __length """
        return self.__length

    @length.setter
    def length(self, value):
        """sets the length attribute with validation"""
        if not isinstance(value (int, float)):
            raise TypeError("length must be a number")
        if value < 0:
            raise ValueError("length must be > 0")

    @property
    def width(self):
        """Getter for __width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width with validation"""
        if value <=0:
            raise ValueError("width must be positive")
            self.__width = value

    def area(self):
        """calculates the rectangle's area"""
        return self.__length * self.__width
       


if __name__ == "__main__":
    rectangle = Rectangle(10, 5)
    print(rectangle.area())    


