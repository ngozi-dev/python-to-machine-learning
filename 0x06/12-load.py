#!/usr/bin/python3
# a module that load and inspect data

import pandas as pd

df = pd.read_csv("file.csv")
print(df.head()) # displays first five info on the dataset
print()

print(df.tail()) # displays the five last info on the dataset
print()
print(df.info())
print()
print(df.describe())
print()
print(df.columns)

