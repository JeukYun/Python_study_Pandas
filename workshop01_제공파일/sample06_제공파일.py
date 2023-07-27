

import pandas as pd
import numpy as np

df = pd.read_csv('./data/sample_data.csv', index_col=0)
print(df)
### 코드 구현 ######
print(df.iloc[0:4, [0,1]])

### 코드 구현 ######