

import pandas as pd
import numpy as np

df = pd.read_csv('./data/sample_data.csv', index_col=0)
print(df)
### 코드 구현 ######
a = df["height"] > 170
print(a)
print(df.loc[a, ['state','height','score']])

### 코드 구현 ######