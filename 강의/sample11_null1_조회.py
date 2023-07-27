import numpy as np
import pandas as pd
## 1. 널(null) 값 조회
'''
     널(null) 값 조회 : None, NaN or NA as null

    1.  Pandas 함수 이용
     1)  bool = pd.isna(스칼라|Series|df)
     2)  bool = pd.isnull(스칼라|Series|df)
     3)  bool = pd.notnull(스칼라|Series|df)

    2.  DataFrame 함수 이용
     1)  bool = df.isnull() >> 전체 검색
         bool = df[컬럼명].isnull() >> 특정 시리즈 검색
         bool = df[[컬럼,컬럼2]].isnull() >> 특정 컬럼 검색

'''

df = pd.DataFrame({ "col1" : [1 ,1, 1, None, 1],
                    "col2" : [2, 2, 2, 2, np.nan],
                    "col3" : [ np.nan, 3, 3, 3, 3],
                    "col4" : [ np.nan, np.nan, np.nan, np.nan, np.nan]},
                    index = [1, 2, 3, 4, 5])
print(df)
'''
   col1  col2  col3  col4
1   1.0   2.0   NaN   NaN  None 으로 입력해도 NaN으로 출력됨
2   1.0   2.0   3.0   NaN
3   1.0   2.0   3.0   NaN
4   NaN   2.0   3.0   NaN
5   1.0   NaN   3.0   NaN
'''
# 1. df대상
print("pd.isna : \n",pd.isna(df))
print()
print("pd.isull : \n",pd.isnull(df))
print()
print("pd.notnull : \n",pd.notnull(df))
print()

# 2. 특정 컬럼(Series) 대상
print("pd.isna(df['컬럼']) : \n",pd.isna(df['col1']))
print()
print("pd.isnull(df['컬럼']) : \n",pd.isnull(df['col1']))
print()

# 3. 특정 컬럼들(DataFrame) 대상
print("pd.isna(df[['컬럼1', '컬럼2']]) : \n",pd.isna(df[['col1', 'col2']]))
print()
print("pd.isnull(df[['컬럼1', '컬럼2']]) : \n",pd.isnull(df[['col1', 'col2']]))
print()

# DataFrame 함수
# 1. df대상
print("df.isnull() : \n",df.isnull()) #pd.isna와 동일
print()
print("df.isna() : \n",df.isna()) #pd.isna와 동일
print()

# 2. 특정 컬럼(Series) 대상
print("df['컬럼명'].isnull() : \n",df['col1'].isnull())
print()

# 3. 특정 컬럼들(DataFrame) 대상
print("df[['컬럼1', '컬럼2']].isnull() : \n", df[['col1', 'col2']].isnull())