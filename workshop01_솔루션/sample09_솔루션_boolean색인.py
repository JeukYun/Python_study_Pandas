

import pandas as pd
import numpy as np

df = pd.read_csv('./data/sample_data.csv', index_col=0)
print(df)
df.loc[df['age'] < 30, 'score'] = 99
print(df)
