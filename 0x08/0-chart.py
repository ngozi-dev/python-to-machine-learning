#!/usr/bin/python3
# a module that displays basic chart types

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x,y, color = "red", marker = "o", linestyle = "--")
plt.title("line plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()
