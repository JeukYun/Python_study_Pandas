import numpy as np
import pandas as pd
## 1. 정렬
'''
   DataFrame 정렬

   1. 정렬
      df.sort_values(by=값, ascending=True, inplace=False, ignore_index=False, 
                     kind="quicksort", na_position="last")

   2. 행 라벨(인덱스) 및 컬럼 라벨(컬럼명) 정렬
      new_df = df.sort_index(axis=0|1)

'''
import seaborn as sns

df = sns.load_dataset("mpg")
print("1. DataFrame")
df = df.head(10)
df.index=list('HDAFCBEGIJ')
# null 변경
df[df['name'] == 'ford torino'] = np.nan

print(df, df.shape) #(398, 9)

# 1. mpg 컬럼 오름차순 정렬
new_df = df.sort_values(by = 'mpg', ascending=True, inplace=False, na_position='first')
print(new_df)

# 2. 다중정렬, mpg 컬럼 오름차순 정렬
new_df = df.sort_values(by = ['mpg','displacement'], ascending=True, inplace=False, na_position='first')
print(new_df)