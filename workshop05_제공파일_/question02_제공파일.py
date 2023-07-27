import pandas as pd
import numpy as np

df = pd.read_csv('./data/employee_sample.csv', index_col=0)
print(df)
### 코드 구현 ######
df_orig = df
df['BONUS'] = [ 10000 if k > 10 else 0  for k in df["YEARS EXPERIENCE"] ]
#df["합격여부"] = ["합격" if n >= 20 else "불합격" for n in df["평균"]]
print(df)
### 코드 구현 ######