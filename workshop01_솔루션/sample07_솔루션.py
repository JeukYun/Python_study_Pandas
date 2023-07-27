

import pandas as pd
import numpy as np

df = pd.read_csv('./data/sample_data.csv', index_col=0)
print(df)
print(df.loc[:'Dean', 'height':])

print(df.loc[:, ['food', 'color']])



print(df.loc['Dean','state'])