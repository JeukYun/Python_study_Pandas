import numpy as np
import pandas as pd
import seaborn as sns

from datetime import datetime
###########################################
### 3.   컬럼과 index 이용한 병합
'''

    컬럼과 index 이용한 병합

     pd.merge(df, df2,  how=“inner”,  left_on=“컬럼명”, right_on = df.index )
     pd.merge(df2, df,  how=“inner”,  left_on=df.index, right_on=“컬럼명” )

     pd.merge(df, df2,  how=“inner”,  left_on=“컬럼명”, right_index=True )
     pd.merge(df2, df,  how=“inner”,  right_on=“컬럼명”, left_index=True )

'''
# 2) 비공통컬럼
df1 = pd.DataFrame({"key":['a','b','a','a','b','c'], "value":range(6)})
df2 = pd.DataFrame({"group_val":[3.5,7]} , index=['a','b'])

print(df1)
'''
  key  value
0   a      0
1   b      1
2   a      2
3   a      3
4   b      4
5   c      5
'''

print(df2)
'''
   group_val
a        3.5
b        7.0
'''

new_df = pd.merge(df1, df2, how="inner", left_on ="key", right_on = df2.index)
print(new_df)
'''
  key  value  group_val
0   a      0        3.5
1   a      2        3.5
2   a      3        3.5
3   b      1        7.0
4   b      4        7.0
'''

new_df = pd.merge(df1, df2, how="inner", left_on ="key", right_index = True)
print(new_df)
'''
  key  value  group_val
0   a      0        3.5
2   a      2        3.5
3   a      3        3.5
1   b      1        7.0
4   b      4        7.0
'''

new_df = pd.merge(df2, df1, how="inner", left_on = df2.index, right_on = "key")
print(new_df)