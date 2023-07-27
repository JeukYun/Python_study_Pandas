import pandas as pd
import numpy as np

df = pd.read_csv('./data/employee_sample.csv', index_col=0)
print(df)
### 코드 구현 ######
df['AGE'] = [40,30,35,25,36,44,50]
print(df)

### 코드 구현 ######