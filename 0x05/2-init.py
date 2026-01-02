#!/usr/bin/python3
# a module that initialize instance attributes

class Square:
    def __init__(self, size = 0):
        self.size = size # public instance attributes


if __name__ == "__main__":
    square = Square(5)
    print(square.size)