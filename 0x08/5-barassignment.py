#!/usr/bin/python3
# a module that displays bar graphs

import matplotlib.pyplot as plt

categories = ['Apples', 'Bananas', 'Cherries']
value = [5, 7, 3]


plt.bar(categories, value)
plt.xlabel("Fruits")
plt.ylabel("Quantity")
plt.title("Fruit Quantity Bar Chart")
plt.show()