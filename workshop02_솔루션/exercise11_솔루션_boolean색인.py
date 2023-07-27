

import pandas as pd
import numpy as np

df = pd.read_csv('./data/stackoverflow_qa.csv')
print(df.head())
print(df[df['ans_name'].isnull() & (df['score'] > 100)])
print(df.loc[df['ans_name'].isnull() & (df['score'] > 100)])
