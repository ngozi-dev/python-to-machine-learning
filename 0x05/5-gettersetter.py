#!/usr/bin/python3
# a module that defines a square class with setter and getter methods

class Square:
    def __init__(self, size=0):
        self.size = size  # invoke the size setter method

    @property # getter method for size
    def size(self):
        """ retrieves the size attribute """
        return self.__size
    
    @size.setter
    def size(self, value):
        """ sets the size attribute with validation """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """ calculates and returns the area of the square """
        return self.__size ** 2
    
if __name__ == "__main__":
    square = Square(-5)
    print(square.area())
    print(square.size)  