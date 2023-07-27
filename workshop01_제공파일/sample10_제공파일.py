

import pandas as pd
import numpy as np

df = pd.read_csv('./data/sample_data.csv', index_col=0)
print(df)
### 코드 구현 ######
df.iloc[1,1] = "RED"
df.iloc[1,3] = 999
df.iloc[1,5] = -1

print(df)

### 코드 구현 ######
