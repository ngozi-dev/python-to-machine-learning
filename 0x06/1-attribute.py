#!/usr/bin/python3
# a module that displays the attributes of an arrays

import numpy as np

c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(c.shape) # dimensions
print(c.dtype) # datatype
print(c.ndim) # number of dimensions

a = np.ones((2, 3, 4))
print(a)
print(a.ndim)