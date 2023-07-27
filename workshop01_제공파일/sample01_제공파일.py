

import pandas as pd
import numpy as np

df = pd.read_csv('./data/sample_data.csv', index_col=0)
print(df)
### 코드 구현 ######
print("1. 인덱스 정보")
print(df.index)

print("2. 컬럼 정보")
print(df.columns)

print("3. 값 정보")
print(df.values)

### 코드 구현 ######
