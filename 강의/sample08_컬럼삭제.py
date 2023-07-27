import numpy as np
import pandas as pd
'''
  
  컬럼삭제
  
  1. 단일컬럼 삭제
    df.pop('컬럼명')
    del df['컬럼명']
    
  2. 다중컬럼 삭제
    df.drop(columns = 리스트)
    df.drop(리스트, axis = 1)

'''

df = pd.DataFrame({"이름":['홍길동','이순신','유관순','강감찬'],
                   "국어":[30, 26, 11, 10],
                   "수학":[20, 12, 20, 12],
                   "영어":[30, 26, 11, 10],
                   "과학":[20, 12, 20, 12],
                   "체육":[20, 12, 20, 12],
                   "보건":[20, 12, 20, 12],
                   "화학":[20, 12, 20, 12],
                   "수리":[20, 12, 20, 12],
                 }, index=[1,2,3,4])

# 1. 단일컬럼 삭제
df.pop("국어")

del df["수학"]
print(df)

# 2. 다중컬럼 삭제
df.drop(columns=["영어", "과학"], inplace= True)
df.drop(["체육", "보건"], inplace= True, axis = 1)
print(df)