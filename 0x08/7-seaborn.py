#!/usr/bin/python3
# a module that plot graphs or chart using seaborn

import seaborn as sns
import pandas as pd

df = sns.load_dataset('tips')
df.head()
sns.boxplot(x = 'day', y = 'total_bill', data = df)

