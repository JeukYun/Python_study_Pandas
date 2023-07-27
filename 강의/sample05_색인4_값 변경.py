import numpy as np
import pandas as pd
'''

'''

df = pd.DataFrame({"col1" : [4 ,5, 6, 6,1],
                   "col2" : [7, 8, 9, 9,2],
                   "col3" : [10, 11, 12, 12,10]},
                   index = list("ABCDE"))
print(df)
'''
   col1  col2  col3
A     4     7    10
B     5     8    11
C     6     9    12
D     6     9    12
E     1     2    10
'''

# 1. A행의 모든 값 변경 (인덱싱)
df.loc['A'] = 100
print(df)

# 2. B,C 행의 모든 값 변경 (fancy)
df.loc[['B','C']] = 200
print(df)

# 3. D행의 col2값 ->> 900
df.loc['D','col2'] = 900
print(df)
#df.iloc[3,1] = 900
#print(df)

# 3. A:D행 col2: col3 값을 -100 변경
df.loc['A':'D', 'col1':'col3'] = -100
print(df)
#################################################
#4. iloc 적용
df.iloc[[0,2], [0,2]] = -1000
print(df)

# 5. boolean 색인 사용 가능
df.iloc[[True,True,True,True,True], [0,2]] = -2000
print(df)