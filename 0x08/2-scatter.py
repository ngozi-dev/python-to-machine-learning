#!/usr/bin/python3
# a module that displays a scatter diagram

import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [10, 20, 30]

plt.scatter(x,y)
plt.title("scatter plot")
plt.grid(True)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()