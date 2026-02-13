#!/usr/bin/python3
# a module that displays bars

import matplotlib.pyplot as plt

x = ["A", "B", "C"]
y = [10, 20, 25]

plt.bar(x,y)
plt.title ("Bar Chart")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()


