import numpy as np
import pandas as pd
####################################################
#### 4. 컬럼 추가 및 삽입
'''
   DataFrame에 컬럼 추가
   ==> 기존 컬럼에 값을 가지고 추가 정보를 얻을 때 사용

  4.  new_df = pd.concat([df,df2], axis=1)
  
  DataFrame에 컬럼 삽입
  
   1. df.insert(idx, 컬럼명, 값 )

'''
df = pd.DataFrame({"이름":['홍길동','이순신','유관순','강감찬'],
                   "국어":[30, 26, 11, 10],
                   "수학":[20, 12, 20, 12]
                 }, index=[1,2,3,4])

df2 = pd.DataFrame({"영어":[30, 26, 11, 10],
                   "과학":[20, 12, 20, 12]
                 }, index=[1,2,3,4])

new_df = pd.concat([df, df2],axis=1)
print(new_df)