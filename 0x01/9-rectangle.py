#!/usr/bin/python3
# a module that calculates the area of a rectangle

def rectangle(length, width):
    return length * width


length = float(input("Enter the lenth of the rectangle:"))
width = float(input("Enter the width of the rectangle:"))
area = rectangle(length, width)
print("The area of the rectangle is: {:.2f}".format(area))
