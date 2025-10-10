#!/usr/bin/python3
# a module that handles area of a circle
import math
radius = float(input("Enter the radius of the circle:"))
area = math.pi * radius ** 2
print("The area of the circle is: {:.2f}".format(area))
