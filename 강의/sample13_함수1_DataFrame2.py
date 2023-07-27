import numpy as np
import pandas as pd
import seaborn as sns

## 3. DataFrame의 기본 함수
'''
   1. 값 변경                                  ==>  df.replace()
   2. 컬럼명 및 인덱스명 변경                     ==> df.rename(columns|index)
   3. 모든(특정) 컬럼(행)값의 참/거짓 여부          ==>  df.any() , df.all()
   4. 중복조회 및 제거                           ==>  df.duplicated(),  df.drop_duplicates()

   5. 임의의 함수 적용 ==> df.apply(함수, axis=0|1)
      임의의 함수를 한번에 DataFrame의 행과 열에 적용.
      이때 함수는 callback형태로 적용

   8. 값이 있으면 True, 아니면 False ==> df.isin(집합형)
      ==> SQL의 in연산자와 동일
      
   9. unique한 값의 갯수 ==> df.nunique(dropna=True)  
                            dropna=False 면 nan 포함해서 갯수 반환
      
      df.nunique ==> 갯수 반환 
      series.unique ==> 값 반환
'''
df = pd.DataFrame({ "a" : [0 ,10, 100],
                    "b" : [2, 20, 200],
                    "c" : [3, 20, 300]},
                    index = list('ABC'))

print("1. DataFrame")
print(df)
'''
     a    b    c
A    0    2    3
B   10   20   20
C  100  200  300
'''


# 1. df.replace(dict, new값) ==> dic에 지정된 값을 new값으로 치환
new_df = df.replace({'a':100, 'b':2, 'c':[20, 300]},999)
print(new_df)
'''
     a    b    c
A    0  999    3
B   10   20  999
C  999  200  999
'''


# 2. df.replace(dict) ==> {old:new, old:new}
new_df = df.replace({20:2000, 3:3000})
print(new_df)
'''
     a     b     c
A    0     2     3
B   10  2000  2000
C  100   200   300
'''



# 3. 컬럼명, 인덱스명 변경
new_df = df.rename(columns = {'a':'col1', 'b':'col2'})
new_df = df.rename(index = {'A':'row1', 'B':'row2'})
print(new_df)
'''
        a    b    c
row1    0    2    3
row2   10   20   20
C     100  200  300
'''


# 4. 모든(특정) 컬럼(행)의 참, 거짓 여부
x = df.all(axis = 0) #모든 컬럼값이 참인지?
x = df.all(axis = 1) #모든 행값이 참인지?
print(x)

x = df.any(axis = 0) #컬럼값이 하나라도 참인지?
x = df.any(axis = 1) #행값이 하나라도 참인지?
print(x)


##################################################
df = pd.DataFrame({"k1":['one']*3 + ['two']*4,
                  "k2":[1,1,2,3,3,4,4] })
print(df)
'''
    k1  k2
0  one   1
1  one   1
2  one   2
3  two   3
4  two   3
5  two   4
6  two   4
'''
# 5. 중복 여부 조회
x = df.duplicated() # df에 중복된 행인지?
print(x)
'''
0    False
1     True
2    False
3    False
4     True
5    False
6     True
'''

# 6. 중복된 행 제거 후 반환
new_df = df.drop_duplicates(ignore_index=True)
print(new_df)
'''
    k1  k2
0  one   1
1  one   2
2  two   3
3  two   4
'''


##################################################################
df = pd.DataFrame({"국어":[50,60,70,80,90],"수학":[100,60,100,100,80]})
print(df)
'''
   국어   수학
0  50  100
1  60  60
2  70  100
3  80  100
4  90  80
'''

# 7. df에 임의의 함수 적용 ==> callback(함수 명만 알려주면 적절한 시점에 실행)
x = df.apply(np.sum, axis = 0)
print(x)
'''
국어    350
수학    440
'''

x = df.apply(np.sum, axis = 1)
print(x)
'''
0    150
1    120
2    170
3    180
4    170
'''


# 8. df.isin(집합형) - 중요, SQL in 연산자와 비슷
new_df = df.isin([60,80]) # df에서 60 또는 80 있는지?
new_df = df.isin({"수학":[60,80]}) # 수학 컬럼에서만 60 또는 80 있는지?
print(new_df)



#########################################################################
df = pd.DataFrame({ "col1" : [1 ,2, 2, None, 1],
                    "col2" : [2, 3, 2, 2, np.nan],
                    "col3" : [ np.nan, 3, 2, 3, 3],
                    "col4" : [ np.nan, np.nan, np.nan, np.nan, np.nan]},
                    index = [1, 2, 3, 4, 5])
print(df)
'''
   col1  col2  col3  col4
1   1.0   2.0   NaN   NaN
2   2.0   3.0   3.0   NaN
3   2.0   2.0   2.0   NaN
4   NaN   2.0   3.0   NaN
5   1.0   NaN   3.0   NaN
'''

# 9. unique한 값의 갯수(종류) 반환 - 기본값 : nan 제외
x = df.nunique(axis=0)
print(x)
'''
col1    2
col2    2
col3    2
col4    0
'''
x = df.nunique(axis=1)
print(x)
'''
1    2
2    2
3    1
4    2
5    2
dtype: int64
'''
x = df.nunique(axis=0, dropna = False) # nan값 포함
print(x)
'''
col1    3
col2    3
col3    3
col4    1
'''

# 10. df.query(조건식) ==> 다른 색인보다 성능이 떨어짐.
df = pd.DataFrame({"국어":[50,60,70,80,90],"수학":[100,60,100,100,80]})
print(df)
'''
   국어   수학
0  50  100
1  60   60
2  70  100
3  80  100
4  90   80
'''

new_df = df.query("국어 > 70")
new_df = df.query("국어 in [50,60,70]")
new_df = df.query("국어 in [50,60,70] and 수학 > 70")
print(new_df)
'''
  국어   수학
3  80  100
4  90   80
'''