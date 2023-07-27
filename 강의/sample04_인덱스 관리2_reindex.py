import numpy as np
import pandas as pd
'''
    인덱스(index) 관리
    0. 인덱스 변경
       df.index = [값, ...]
    
    1. df.set_index(기존컬럼, inplace = True/False)
       df.reset_index(drop = True/False, inplace = True/False)
       
    2. df.reindex(index = 값)
       ==> 기존 인덱스 재배치
           
'''
df = pd.DataFrame({    "date":['2021','2022','2023','2024','2025'],
                       "City": ["Seoul", "Seoul", "Seoul", "Seoul", "Seoul"],
                       "Temperature": [32, 34, 35, 36, 37]
                       }, index=list('AECBD'))
print("1. 원본 DataFrame")
print(df)

# 3. 인덱스 재배치
new_df = df.reindex(index = list('ABCDE'))
print(new_df)