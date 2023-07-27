

import pandas as pd
import numpy as np

df = pd.read_csv('./data/stackoverflow_qa.csv')
print(df.head())
print(df[df['quest_name'] == df['ans_name']].head())
print(df.loc[df['quest_name'] == df['ans_name']].head())

