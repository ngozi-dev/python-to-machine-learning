#!/usr/bin/python3
# a module that creates 2D arrays

import numpy as np

y = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
print(y[[1][0]])
print(y[0] * [0])
print(y[0] * [1])
print(y[0] * [2])
print(y[0] * [-2])
print(y[0] * [-1])

values = np.arange(1, 6)
rows = np.arange(1, 6).reshape(5, 1)
print(rows * values)