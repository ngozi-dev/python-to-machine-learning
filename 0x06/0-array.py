#!/usr/bin/python3
# a module that creates an array with NumPy

import numpy as np

a = np.array([1, 2, 3]) # one dimensional array
b = np.array([[1, 2], [3, 4]]) # two dimensional array
c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # three dimensional array
d = np.zeros((2, 3)) # creating zeros in 2 by 3
e = np.ones((3, 1)) # creating ones in 3 by 1
f = np.arange(0, 10, 2) # indicates range of numbers and their step
g = np.linspace(0, 1, 5) # indicates the start number, end number and the step
h = np.linspace(2, 5, 4) # linspace is determined by the subtracting
                        # the starting point from the ending point, divide by the step value minus one
# out put from variables
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)

i = np.array([[1, 2, 3], [4, 5, 6]])
print()