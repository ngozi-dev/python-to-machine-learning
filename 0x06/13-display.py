#!/usr/bin/python3
# a module that loads and displays data

import pandas as pd

df = pd.read_csv("staffrecords.csv")
print(df.head(1))
print()
print(df.tail())
print()
print(df.loc[0])

print()

print(df.describe())


# The Python pandas function DataFrame
# . describe()
# is used to generate a statistical summary of
# the numerical columns in a DataFrame. 
# This summary includes key statistical metrics
# like mean, standard deviation, minimum, 
# maximum and different percentiles.




