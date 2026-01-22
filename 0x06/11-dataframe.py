#!/usr/bin/python3
# a module that handles data frame

import pandas as pd

data = {
    "name" : ["ngozi", "chioma", "emeka", "taiwo"],
    "age" : [34, 50, 30, 48]

}
df = pd.DataFrame(data)
print(df)


