import numpy as np
import pandas as pd
####################################################
#### 6. 행 추가 및 삭제
'''
   DataFrame 행(row) 추가

  1. 한번에 하나씩 추가 
    new_df = df_append(df2, ignore_index=True)

  2. 한번에 여러개 추가
    new_df = pd.concat([df,df2,..], axis=0 , ignore_index=True)


      DataFrame 행 삭제

   1. new_df = df.drop(index=[인덱스명, 인덱스명])

   2. new_df = df.drop([인덱스명, 인덱스명], axis=0)
'''

# 1. 한번에 하나씩 추가
info={"Name":["유관순","안중근"],"age":[18,31],"birthday":['1920/09/28','1910/03/26']}
df = pd.DataFrame(info)

info2 = {"Name":["홍길동","강감찬"],"age":[22,43],"birthday":['1990/09/28','1980/03/26']}
df2 = pd.DataFrame(info2)

print(df)
print(df2)

new_df= df._append(df2, ignore_index=True)
print(new_df)

# 2. 한번에 여러개 추가
new_df2 = pd.concat([df,df2,df2,df2], ignore_index=True) # axis 기본값 = 0
print(new_df2)