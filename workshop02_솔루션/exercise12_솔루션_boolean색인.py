

import pandas as pd
import numpy as np

df = pd.read_csv('./data/stackoverflow_qa.csv')
print(df.head())

print(df[df['answercount'].between(5, 10) & (df['viewcount'] < 1000)].head())
print(df.loc[df['answercount'].between(5, 10) & (df['viewcount'] < 1000)].head())