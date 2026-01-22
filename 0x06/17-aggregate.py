#!/usr/bin/python3
# a module that perform grouping and aggregation 

import pandas as pd

df = pd.read_csv("Employee_Data.csv")
df_grouped = df.groupby("Department")  # Group the DataFrame by the 'Department' column
print(df_grouped["Department"].count())  # Count the number of records in each department
print(df_grouped["Salary"].mean())  # Calculate the mean salary for each department
print(df_grouped.agg({"Salary": ["min", "max", "mean"]}).sort_index())    # Aggregate min, max, and mean salary for each department



