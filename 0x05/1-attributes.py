#!/usr/bin/python3
# a module that creats a class and include their attributes

class Square:
    size = 0 #public class attributes
    __area = 0 # private class
    _dimension = (0,0) # protected class attributes


if __name__ == "__main__":
    square = Square()
    print(square.size)
    try:
        print(square.__area)
    except Exception as e:
        print("Area is a private class attributes")
    print(square._dimension)
    print(dir(square))

