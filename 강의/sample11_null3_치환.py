import numpy as np
import pandas as pd
## 3. 널(null) 값 변경
'''
     null 값 변경

     1. 변경
        df.fillna(value, method='bfill|ffill|None', inplace=False, limit=n )
                                  뒷값   앞값


'''

df = pd.DataFrame({ "col1" : [1 ,1, 1, 1, np.nan],
                    "col2" : [2, 2, 2, 2, np.nan],
                    "col3" : [3, 3, 3, 3, np.nan],
                    "col4" : [ np.nan, np.nan, np.nan, np.nan, np.nan]},
                    index = [1, 2, 3, 4, 5])
print(df)
'''
   col1  col2  col3  col4
1   1.0   2.0   3.0   NaN
2   1.0   2.0   3.0   NaN
3   1.0   2.0   3.0   NaN
4   1.0   2.0   3.0   NaN
5   NaN   NaN   NaN   NaN
'''
print()

# 1. 전체 df의 null값을 임의의 값(0)으로 변경 ==> 일반적으로 평균을 사용한다.
new_df = df.fillna(0)
print("df.fillna(0)\n",new_df)
print()

# 2. 컬럼마다 다르게 null값을 임의의 값으로 변경
new_df = df.fillna({'col1':-1, 'col2':-2})
print("df.fillna({'col1':-1, 'col2':-2})\n",new_df)
print()

# 3. null의 앞(forword)값으로 변경
df = pd.DataFrame({ "col1" : [1 ,np.nan, 3, 4, np.nan],
                    "col2" : [1 ,np.nan, 3, 4, np.nan],
                    "col3" : [1 ,2, np.nan, 4, np.nan]},
                    index = [1, 2, 3, 4, 5])
print(df)
print()
'''
   col1  col2  col3
1   1.0   1.0   1.0
2   NaN   NaN   2.0
3   3.0   3.0   NaN
4   4.0   4.0   4.0
5   NaN   NaN   NaN
'''
new_df = df.fillna(method='ffill')
print("df.fillna(method='ffill')\n",new_df)
print()

# 4. null의 뒤(back)값으로 변경
new_df = df.fillna(method='bfill')
print("df.fillna(method='bfill')\n",new_df)
print() # 마지막 행의 값은 채워지지 않고 NaN으로 남음