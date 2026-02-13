#!/usr/bin/python3
# a module that displays histogram plots

import matplotlib.pyplot as plt

item = [1,2,2,3,3,3,4,4,4,4]
plt.hist(item, bins = 4)
plt.title("histogram plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()