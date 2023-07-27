

import pandas as pd
import numpy as np

df = pd.read_csv('./data/sample_data.csv', index_col=0)
print(df)
print(df.loc[['Dean', 'Cornelia'], ['age', 'state', 'score']])  # multi rows , multi column

print(df.loc[['Dean', 'Aaron'], 'food']) # multi rows , single column
print(df.loc['Dean', 'food']) # single rows , single column => Cheese