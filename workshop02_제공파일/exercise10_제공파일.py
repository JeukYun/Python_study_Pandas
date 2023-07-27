

import pandas as pd
import numpy as np

df = pd.read_csv('./data/stackoverflow_qa.csv')
print(df.head())
### 코드 구현 ######
a = df['quest_name'] == df['ans_name']
print(df[a][0:7].loc[:,['id','score','score', 'quest_name', 'ans_name']])

### 코드 구현 ######
