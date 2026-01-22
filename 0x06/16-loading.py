#!/usr/bin/python3
# a module that loads a dataset into a pandas DataFrame

import pandas as pd

# No.1 Loading & Inspecting Data

df = pd.read_csv("studentsinfo.csv")
print(df.head(10)) # Display the first 10 records
print(df.shape)  # Display the shape of the DataFrame (rows, columns)
print(df.columns)  # Display the column names
print(df.dtypes)  # Display the data types of each column
print()

# No.2 Selecting & Filtering columns

print(df[["name", "age" , "score"]])  # Display the column with names, age and score
print(df.score > 75)  # Display boolean series where score is greater than 75
print(df[df.score > 75])  # Display records where score is greater than 75
print()

# No.3 Conditional Filtering

print(df[(df.age > 20) & (df.score < 50)])  # Display records where age is greater than 20 and score is less than 50
print(df[["name", "score"]]) # Display only the names and scores of students whose age is greater than 20 and score is less than 50
print()

# No.4 Cleaning Operations
df_cleaned = df.dropna()  # Remove records with missing values
print(df_cleaned)   # Display the cleaned DataFrame


