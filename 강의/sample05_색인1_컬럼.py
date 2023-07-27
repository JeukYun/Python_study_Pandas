import numpy as np
import pandas as pd
'''
   * 컬럼 선택 (SQL의 projection기능)
   가.  [] : 인덱싱 연산자, 컬럼(들)을 선택하는 목적
           예> [컬럼] ==> Series 반환 ( index와 값 으로 구성됨 )
              [[컬럼,컬럼]] ==> DataFrame 반환
              
     ==> 단일컬럼 조회
         df['컬럼명'] or df.컬럼명 : Series 반환
                  
         다중컬럼 조회
         df[['컬럼명','컬럼명']] : DataFrame 반환
'''

# 1. 싱글 및 멀티 컬럼 조회
df = pd.DataFrame({"col1" : [4 ,5, 6, 6],
                   "col2" : [7, 8, 9, 9],
                   "col3" : [10, 11, 12, 12]},
                   index = list("ABCD"))

print("1. col1 컬럼만 조회")
print(df.col1 )     # Series 반환

print("2. col1 컬럼만 조회")
print(df['col1'])  # Series 반환

print("3. col1와 col2 컬럼 조회")
print(df[['col2', 'col1']])  # fancy 색인 비슷 , # DataFrame 반환

print("4. col1 컬럼만 여러번 조회")
print(df[['col1','col1','col1']])  # DataFrame 반환