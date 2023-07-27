

import pandas as pd
import numpy as np

df = pd.read_csv('./data/stackoverflow_qa.csv')
print(df.head())

### 코드 구현 ######
print(df[df['answercount'].between(0,5) & (df['viewcount'] <1000)].head())
### 코드 구현 ######