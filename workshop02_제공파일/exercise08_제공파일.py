

import pandas as pd
import numpy as np

df = pd.read_csv('./data/stackoverflow_qa.csv')
print(df.head())
### 코드 구현 ######
a = df["answercount"] == 5
print(df.loc[a][0:5])
### 코드 구현 ######
