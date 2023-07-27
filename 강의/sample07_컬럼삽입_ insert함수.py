import numpy as np
import pandas as pd
####################################################
#### 4. 컬럼 추가 및 삽입
'''
  
  DataFrame에 컬럼 삽입
  
   1. df.insert(idx, 컬럼명, 값 )

'''
df = pd.DataFrame({"이름":['홍길동','이순신','유관순','강감찬'],
                   "국어":[30, 26, 11, 10],
                   "수학":[20, 12, 20, 12]
                 }, index=[1,2,3,4])

df.insert(1,"영어",df["수학"])
print(df)