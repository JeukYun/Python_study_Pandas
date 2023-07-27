import numpy as np
import pandas as pd
'''
    DataFrame의 컬럼과 인덱스 변경
    
        1. 컬럼정보 
        df.columns 또는 df.keys()
        
        2. 인덱스(라벨) 정보
        df.index
        
        3. 값 정보
        df.values 
        또는 
        df.to_numpy() -> 권장
'''

'''
   col1  col2  col3
0     4     7    10
1     5     8    11
2     6     9    12
'''
df = pd.DataFrame({"col1" : [4 ,5, 6],
                   "col2" : [7, 8, 9],
                   "col3" : [10, 11, 12]}, index=['A','B','C'])
# 1. 컬럼정보 보기
print(df.columns)
print(df.keys())

# 2. 인덱스 정보
print(df.index)

# 3. 값 보기 ==> 다차원 배열로 반환
print(df.values)
print(df.to_numpy())