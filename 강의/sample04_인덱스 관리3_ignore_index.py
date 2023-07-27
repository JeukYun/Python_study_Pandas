import numpy as np
import pandas as pd
'''
    인덱스(index) 관리
    
    3. ignore_index = True
       ==> df와 df2 연결 시 인덱스도 연결이 돼서 중복됨.
           이때 인덱스 제외하여 연결하는 방법
           ( 자동으로 인덱스 생성 )       
'''
# 4. df병합시 기존 index값이 중복발생 ==> ignore_index=True 로 index값을 재설정
df1 = pd.DataFrame({'a':[12,2]},
                   index=[1,2])
df2 = pd.DataFrame({'a':[120,20]},
                   index=[1,2])

new_df = pd.concat([df1, df2])
print(new_df)

new_df2 = pd.concat([df1, df2], ignore_index=True)
print(new_df2)