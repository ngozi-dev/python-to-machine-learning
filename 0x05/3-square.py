#!/usr/bin/python3
# a module that defines a class and handles errors gracefully

class Square:
    def __init__ (self, size = 0):
        if not isinstance(size, (int, float)):
            raise TypeError("size must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size  # create a public instance attribute size
    def area (self): # create a public method that returns/calculates the area of a square
        return self.size ** 2
    
if __name__ == "__main__":
    square = Square(-5)
    print(square.area())


