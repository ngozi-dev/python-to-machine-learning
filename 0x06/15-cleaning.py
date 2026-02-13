#!/usr/bin/python3
# a module that cleans datasets using operations methods

import pandas as pd

df = pd.read_csv("Employee_Data.csv") # 
df.dropna() # to remove rows that have missing values
df.fillna(0) # this will replace not a "na" or "nan" not a number value with zero
a = df.drop(columns = ["Name", "Salary"]) # to drop a column
print(a)

df.rename(columns={"Name": "Emp_Name", "Salary": "Emp_Salary"},inplace=True)    # to rename columns
print(df)
df["Emp_Salary"] = df["Emp_Salary"].astype(float)  # to change the datatype of a column
print(df["Emp_Salary"].head(5))
print(df.dtypes)


# to convert all names to uppercase
print(df["Emp_Name"].str.upper())


