

import pandas as pd
import numpy as np
pd.set_option('display.max_columns', 10)
df = pd.read_csv('./data/food_inspections.csv')
#print(df.head())
### 코드 구현 ######
df.set_index("DBA Name", inplace=True)
print(df.loc['THRESHOLD SCHOOL':'SCRUB A DUB':3000, 'Inspection Type':])
### 코드 구현 ######
