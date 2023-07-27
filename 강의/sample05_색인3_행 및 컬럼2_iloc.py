import numpy as np
import pandas as pd
'''
    * 행과 조회

   다.  .iloc[] :   loc와 유사하지만 정수위치값만을 사용한다.
                  행과 컬럼 모두 위치값 만 사용 가능하다.
'''
## 3) 행 및 컬럼 조회
'''
   DataFrame 의 행과 컬럼 조회 

    2. 행 인덱스의 위치 이용
    ==> 기본 문법은 df.iloc[행위치, 컬럼위치]

'''

df = pd.DataFrame({"col1" : [4 ,5, 6, 6,1],
                   "col2" : [7, 8, 9, 9,2],
                   "col3" : [10, 11, 12, 12,10]},
                   index = list("ABCDE"))
print(df)
'''
    0      1      2
   col1  col2  col3
A     4     7    10
B     5     8    11
C     6     9    12
D     6     9    12
E     1     2    10
'''
# 1. 인덱싱
print(df.iloc[0, 0]) # 4 츨력 >> 스칼라값

# 2. 인덱싱 + fancy
print(df.iloc[[0,1], 0]) # Series 반환

# 3. fancy + fancy
print(df.iloc[[0,1], [0, 1]]) # DataFrame 반환

# 4. slice + fancy
print(df.iloc[1 : ,[0, 1]]) #DataFrame 반환

# 5. slice + slice
print(df.iloc[1 : , 1 : ]) #DataFrame 반환

# 6. boolean + slice
print(df.iloc[[True, False, True, False, True], 1 : ]) #DataFrame 반환
