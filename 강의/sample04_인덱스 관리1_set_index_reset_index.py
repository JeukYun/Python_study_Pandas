import numpy as np
import pandas as pd
'''
    인덱스(index) 변경
     - DataFrame의 기존컬럼을 index로 변경
     - inplace=True|False 에 따라서 복사여부 결정
     문법:
           df.set_index(기존컬럼, inplace=True|False)

           df.reset_index( drop=False, inplace=True ) # 기존 index를 컬럼으로 변경하고 새로운 index 생성
           df.reset_index( drop=True, inplace=True ) # 기존 index를 삭제하고 새로운 index 생성
           
'''
df = pd.DataFrame({    "date":['2021','2022'],
                       "City": ["Seoul", "Seoul"],
                       "Temperature": [32, 34]
                       })
print("1. 원본 DataFrame")
print(df)

# 1) 기존 컬럼을 인덱스로 변경
print("기존 컬럼을 인덱스로 변경")
df.set_index('date', inplace=True)
print(df)
print(df.index)

# 2) 기존 인덱스를 컬럼으로 변경하고 새로운 인덱스 생성
#df.reset_index(drop=False, inplace=True)
#print(df)
# 3) 기존 인덱스를 삭제하고 새로운 인덱스 생성
df.reset_index(drop=True, inplace=True)
print(df)