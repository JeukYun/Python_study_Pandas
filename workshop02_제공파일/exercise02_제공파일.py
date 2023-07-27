

import pandas as pd
import numpy as np
#pd.set_option('display.max_columns', 10)
df = pd.read_csv('./data/food_inspections.csv')
print(df.head())
#'WILD GOOSE BAR & GRILL'
### 코드 구현 ######
df.set_index("DBA Name", inplace=True)
print(df.loc['WILD GOOSE BAR & GRILL'])
### 코드 구현 ######