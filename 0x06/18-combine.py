#!/usr/bin/python3
# a module that combine two pandas DataFrames

import pandas as pd

df1 = pd.DataFrame({"ID": [1, 2, 3], "Name": ["Ngozi", "Chioma", "Rash"]}) 
df2 = pd.DataFrame({"ID": [4, 5, 6], "Name": ["Emeka", "Ifeanyi", "Kelechi"]})
combine = pd.concat([df1, df2], ignore_index=True) # Combine the two DataFrames
#print(combine)

#merged = pd.merge(df1, df2, on="ID", how="inner")  # Merge the two DataFrames on the 'ID' column
merged = pd.merge(df1, df2, on="ID", how="outer")  # Outer merge the two DataFrames on the 'ID' column  
#merged = pd.merge(df1, df2, on="ID", how="left")   # Left merge the two DataFrames on the 'ID' column
#merged = pd.merge(df1, df2, on="ID", how="right")  # Right merge the two DataFrames on the 'ID' column
#merged = pd.merge(df1, df2, on="ID", how="cross")  # Cross merge the two DataFrames on the 'ID' column
print(merged)

