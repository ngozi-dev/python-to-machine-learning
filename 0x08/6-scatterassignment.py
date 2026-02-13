#!/usr/bin/python3
# a module that displays scatter plots with assigned colors and sizes

import matplotlib.pyplot as plt

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]

plt.plot(x,y, color = "red", marker = "x", linestyle = "--")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Scatter Plot Example")
plt.show()
