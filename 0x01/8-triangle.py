#!/usr/bin/python3
# a module that calculates the area of a triangle

def triangle(base, height):
    return 0.5 * base * height


base = float(input("Enter the base of the triangle:"))
height = float(input("Enter the height of the triangle:"))
area = triangle(base, height)
print("The area of the triangle is: {:.2f}".format(area))