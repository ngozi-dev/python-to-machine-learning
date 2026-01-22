#!/usr/bin/python3
# a module that structure data in one dimension

import pandas as pd

s = pd.Series([10, 20, 30, 40], index = ["a", "b", "c", "d" ])
print(s)
print(s["b"])