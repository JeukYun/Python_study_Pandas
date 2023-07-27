

import pandas as pd
import numpy as np

df = pd.read_csv('./data/food_inspections.csv')
print(df.head())
### 코드 구현 ######
df.set_index("DBA Name", inplace= True)
print(df.iloc[[100,1000,10000],[5,3,1]])

### 코드 구현 ######