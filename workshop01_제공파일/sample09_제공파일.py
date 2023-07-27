

import pandas as pd
import numpy as np

df = pd.read_csv('./data/sample_data.csv', index_col=0)
print(df)
### 코드 구현 ######
a = df['age']<30
print(a)
df.loc[a, "score"] = 99
print(df)

### 코드 구현 ######