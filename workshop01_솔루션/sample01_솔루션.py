

import pandas as pd
import numpy as np

df = pd.read_csv('./data/sample_data.csv', index_col=0)
print(df)
print("1. 인덱스 정보: \n", df.index)
print("2. 컬럼 정보: \n", df.columns)
print("3. 값 정보: \n", df.values)