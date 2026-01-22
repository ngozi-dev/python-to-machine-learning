#!/usr/bin/python3
# a module that select items and filter them

import pandas as pd

df = pd.read_csv("Employee_Data.csv")
#print(df["Salary"]) # To select just a column ie "Salary"

#print(df[["Name", "Salary"]]) # selecting multiple columns

#print(df.iloc[1])
#print(df.loc[1])

print(df[df["Salary"]> 300000])
