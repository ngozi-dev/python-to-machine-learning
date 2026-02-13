#!/usr/bin/python3
# a module that displays line graphs

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

plt.plot(x, y, color = "red", marker = "o", linestyle = "solid")
plt.title("Simple Line")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()


