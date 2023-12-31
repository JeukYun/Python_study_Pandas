import numpy as np
import pandas as pd
'''
    * 행조회
   나.  .loc[] :  label만을 사용한다. ( 기본적으로 index의 label로 인식 )
               label은 single, list, slice 형태 모두 가능하다.
               행과 열을 동시에 조회할 수 있다. df.loc[행,열]
               행과 컬럼 모두 label 만 사용 가능하다.
               
   다.  .iloc[] :   loc와 유사하지만 정수위치값만을 사용한다.
                  행과 컬럼 모두 위치값 만 사용 가능하다.
'''
## 2) 행 조회
'''
    2. 행 인덱스의 위치 이용
      - df.iloc[위치]                  ==> 인덱싱 위치, Series 반환
      - df.iloc[[위치,위치1,...]]       ==> fancy 위치, DataFrame 반환
      - df.iloc[위치:위치2]             ==> slicing 위치, DataFrame 반환
                                      ==> 위치2 포함안됨. (기존 python문법 따름)
      - df.iloc[[True,False,..]]      ==> boolean 색인  
'''
df = pd.DataFrame({"col1" : [4 ,5, 6, 6,1],
                   "col2" : [7, 8, 9, 9,2],
                   "col3" : [10, 11, 12, 12,10]},
                   index = list("ABCDE"))
print(df)
''' # 원본 #
         col1  col2  col3
0   A     4     7    10
1   B     5     8    11
2   C     6     9    12
3   D     6     9    12
4   E     1     2    10
'''
## df.iloc
print("1. A 행 출력(인덱싱 위치)")
print(df.iloc[0]) # Series 반환
print("2. A 와 B행 출력(fancy 위치)")
print(df.iloc[[0,1]]) # DataFrame 반환
print("3. B행부터 D행까지 출력(slicing label)")
print(df.iloc[1:-1]) # DataFrame 반환
print("4. A,C,E행 출력(boolean label)")
print(df.iloc[[True,False,True,False,True]]) # DataFrame 반환


## 조회후 값 변경
df = pd.DataFrame({"col1" : [4 ,5, 6, 6,1],
                   "col2" : [7, 8, 9, 9,2],
                   "col3" : [10, 11, 12, 12,10]},
                   index = list("ABCDE"))
print(df)
