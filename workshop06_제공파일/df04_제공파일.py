

import numpy as np
import pandas as pd

sp500 = pd.read_csv("./data/sp500.csv",
                    index_col='Symbol',
                    usecols=[0, 2, 3, 7])

# print(sp500.head())
sp500.rename(columns={'Book Value': 'BookValue'},
             inplace=True)
sp500_copy = sp500.head().copy()
### 코드 구현 ######
a = {"Symbol":["SAMSUNG","LG"], "Sector":["Industrials", "Industrials"],
     "Price":[40.32, 39.20], "BookValue":[12.300, 3.220]}
SAMSUNG = pd.DataFrame(a)
SAMSUNG.set_index("Symbol",inplace=True)
print(SAMSUNG)

sp500_copy = pd.concat([sp500_copy,SAMSUNG])
### 코드 구현 ######

print(sp500_copy)