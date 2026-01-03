#!/usr/bin/python3
# a module that computes the square of numbers from a file

class Square:
    def __init__(self, size):
        self.size = size

    def area(self):
        return self.size **2


if __name__ == "__main__":
    square = Square(5)
    print(square.area())
    
