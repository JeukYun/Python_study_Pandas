import numpy as np
import pandas as pd
'''
    DataFrame의 컬럼과 인덱스 변경
    
    1. 컬럼명 변경
        df.columns = [값, 값2 , ...]
    
    2. 인덱스(라벨) 변경
        가. pd.DataFrame(....., index = [값, 값2 , ...)
        나. index = [값, 값2 , ...]
'''

'''
   col1  col2  col3
0     4     7    10
1     5     8    11
2     6     9    12
'''
df = pd.DataFrame({"col1" : [4 ,5, 6],
                   "col2" : [7, 8, 9],
                   "col3" : [10, 11, 12]})
print(df)

# 1. 컬럼명 변경
df.columns = ['c1', 'c2', 'c3']
print("1. 컬럼명 변경", df)
''' 
   c1  c2  c3
0   4   7  10
1   5   8  11
2   6   9  12
'''

# 2. 인덱스(라벨) 변경
df = pd.DataFrame({"col1" : [4 ,5, 6],
                   "col2" : [7, 8, 9],
                   "col3" : [10, 11, 12]}, index=['A','B','C'])
print("2-1. 인덱스(라벨) 변경", df)

df.index = [10, 20, 30]
print("2-2. 인덱스(라벨) 변경", df)