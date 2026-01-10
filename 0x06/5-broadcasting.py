#!/usr/bin/python3
# a module that allow operations between arrays of different shapes


import numpy as np

a = np.array([[1], [2], [3]])
b = np.array([10, 20, 30])
print(a + b)
print(np.sum(b))
print(np.max(b))
print(np.min(b))
print(np.std(b))
print(np.mean(b))
print(np.dot(b, 2))
