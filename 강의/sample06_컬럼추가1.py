import numpy as np
import pandas as pd
####################################################
#### 4. 컬럼 추가 및 삽입
'''
   DataFrame에 컬럼 추가
   ==> 기존 컬럼에 값을 가지고 추가 정보를 얻을 때 사용

  1. df['컬럼명'] = 리스트   >> 가장 일반적인 예
      df['컬럼명'] = Series

  2.  new_df = df.assign(컬럼명=리스트)

  3.  new_df = df.assign(컬럼명=함수, 컬럼명=함수)

  4.  new_df = pd.concat([df,df2], axis=1)
  
  DataFrame에 컬럼 삽입
  
   1. df.insert(idx, 컬럼명, 값 )

'''

df = pd.DataFrame({"이름":['홍길동','이순신','유관순','강감찬'],
                   "국어":[30, 26, 11, 10],
                   "수학":[20, 12, 20, 12]
                 }, index=[1,2,3,4])

print("1. DataFrame")
print(df)
''' #원본#
    이름  국어  수학
1  홍길동  30  20
2  이순신  26  12
3  유관순  11  20
4  강감찬  10  12
'''

# 1. df['컬럼명'] = 리스트
df['영어'] = [10,20,30,40]
print(df)

# 2. df['컬럼명'] = Series
df["과학"] = pd.Series(data = [10,20,30,40], index = [1,2,3,4])
print(df)
# DataFrame의 인덱스가 1,2,3,4 라서 Series의 1,2,3만 들어감
# Series로 DataFrame 추가시 index지정 필요!!

df["종합"] = df['국어'] + df['수학'] + df['영어'] + df['과학']
print(df)

df['평균'] = np.round(df["종합"]/4,1)
print(df)

# 평균 ==> series에 데이터 타입을 변경하는 함수
df['평균'] = df['평균'].astype(np.int32)
print(df)

# 실습 : 평균이 20보다 크면 '합격', 작으면 '불합격'
df["합격여부"] = ["합격" if n >= 20 else "불합격" for n in df["평균"]]
    #['합격' if df['평균']>20 else '불합격']
print(df)