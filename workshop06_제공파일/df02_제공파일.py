

import numpy as np
import pandas as pd

sp500 = pd.read_csv("./data/sp500.csv",
                    index_col='Symbol',
                    usecols=[0, 2, 3, 7])

print(sp500.head())
### 코드 구현 ######
sp500_copy = sp500
sp500_copy['RoundedPrice'] = sp500_copy["Price"].round()
sp500_copy.insert(1,"RoundedPrice2", sp500_copy["Price"].round())
### 코드 구현 ######
print(sp500_copy.head())
