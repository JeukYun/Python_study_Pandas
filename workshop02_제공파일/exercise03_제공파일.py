

import pandas as pd
import numpy as np

df = pd.read_csv('./data/food_inspections.csv')
print(df.head())
df = df.set_index('DBA Name')
### 코드 구현 ######
print(df.loc[["WILD GOOSE BAR & GRILL","TAQUERIA HACIENDA TAPATIA"],["Risk","Results"]])

### 코드 구현 ######