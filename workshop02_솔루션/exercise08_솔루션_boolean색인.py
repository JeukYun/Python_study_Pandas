

import pandas as pd
import numpy as np

df = pd.read_csv('./data/stackoverflow_qa.csv')
print(df.head())
print(df[df['answercount'] == 5].head())
print(df.loc[df['answercount'] == 5].head())
