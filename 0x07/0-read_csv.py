#!/usr/bin/python3
# a module that reads a csv file

import pandas as pd

df = pd.read_csv("ngrecords.csv")
#print(df)
#print(df.head(2))  # displays first two info on the dataset
#print(df.shape)  # displays the shape of the dataset (rows, columns)
#print(df.columns)  # displays the column names
#print(df.dtypes)  # displays the data types of each column
#print(df['name'])  # displays the 'name' column
#print(df[df["AGE"] > 30])  # displays rows where age is greater than 30
#print(df.describe())  # displays summary statistics of numeric columns
#print(df.sum(numeric_only=True))  # displays the sum of numeric columns
#print(df.sum("DEPT", numeric_only=True))   # displays the sum of the 'DEPT' column


# N0 1: Write a line of code to filter only rows where age > 30 and display the result

print(df[df.AGE > 30])  # alternative way to display rows where age is greater than 30


# No 2: Write a line of code to group a DataFrame by a category column and compute the sum of a value column

print(df.groupby(["DEPT"]).size())  # displays the count of records in each department

# N0 2ii displays the sum of the 'DEPT' column

print(df.groupby("DEPT").sum(numeric_only=True)) 


# No 3: Write code to compute the total sales for each product in each region, as new DataFrame

df = pd.DataFrame({
    'product': ['A', 'B', 'A', 'B', 'A'],
    'region': ['East', 'West', 'East', 'West', 'North'],
    'sales': [100, 200, 150, 250, 120]
})

total_sales = df.groupby(['product', 'region'])['sales'].sum().reset_index()
print(total_sales)  # displays the total sales for each product in each region
