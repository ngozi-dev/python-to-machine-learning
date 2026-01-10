#!/usr/bin/python3
# a module that slice an array

import numpy as np

y = np.array([[2, 3, 4], [5, 6, 7]])
print(y[1, -1])
print(y[0, 1], y[1, 1])
print(y[:, 1])