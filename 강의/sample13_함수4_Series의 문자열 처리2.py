import numpy as np
import pandas as pd
import seaborn as sns

## 3. Series의 문자열 처리
'''
    1. 문법 : series.str.함수
    
    * 문자열 관련 함수
    1) python
        - 문자열.함수
        예> "hello".upper()
    2) numpy
        arr = np.array(['aa', 'Bb', 'cc'])
        => np.char.함수명
        
    3) pandas
        series.str.함수

'''

info={"name":["Hello","Happy","Cat"],
      "age":[18,31, 33],
      "birthday":['1920/09/28','1910/03/26','2020/03/26']}
df = pd.DataFrame(info)
print(df)

'''
    name  age    birthday
0  Hello   18  1920/09/28
1  Happy   31  1910/03/26
2    Cat   33  2020/03/26
'''

# 1. series.str.replace함수
df['name1'] = df['name'].str.replace("Hello", "Hello".lower())
print(df)

# 2. 인덱싱 및 slice
#df['name2'] = df['name'].str[::-1]
df['name2'] = df['name'].str[1:3]
df['name3'] = df['name'].str[0]
print(df)

# 3. str.upper, str.lower
df['name4'] = df['name'].str.upper()
df['name5'] = df['name'].str.lower()
print(df)

# 4. contains(값|값2) - 중요
df['name6'] = df['name'].str.contains('a')
df['name7'] = df['name'].str.contains('a|e')
print(df)

#실습 : name컬럼에서 a 포함 된 데이터 출력
print(df['name'][df['name'].str.contains('a')])
xxx = df['name']
print(xxx[xxx.str.contains('a')])

# 5. H로 시작하는 데이터 출력
df['name8'] = df['name'].str.startswith('H')
print(df)


# 6. islower ==> boolean인덱스
df['name9'] = df['name'].str.islower()
print(df)

# 7. one-hot 인코딩 변환
# 머신러닝, 딥러닝에서 순서(1,2,3) 부여시 가중치로 받아들일 수 있어
# 아래와 같이 처리
pets = pd.Series(['Cat','Dog','Birds'])
print(pets.str.get_dummies())