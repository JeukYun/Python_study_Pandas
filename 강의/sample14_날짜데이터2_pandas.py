import numpy as np
import pandas as pd
import seaborn as sns

from datetime import datetime
###########################################
### 1.  Pandas 이용한 날짜 데이터 처리
'''
    날짜 데이터 처리

   1. str --> datetime로 변환
      pd.to_datetime('날짜', format = " ")

  2. datetime을 지정된 범위에서 반환
      pd.date_range('날짜', '날짜')

   3.  DatetimeProperties 속성 이용한 날짜 정보 구하기
      df['xxx'].dt.year -->> df['xxx']가 날짜 형식이어야 함

   4. datetime --> str로 변환
      df['xxx'].astype(str)
'''
from datetime import datetime

# 1. str --> datetime

# 가. 기본적으로 날짜로 인식 가능한 형식
xxx = pd.to_datetime('2023/06/15')
xxx = pd.to_datetime('2023-06-15')
xxx = pd.to_datetime('2023 06 15')

# 나. 명시적으로 날짜로 인식해야하는 형식
xxx = pd.to_datetime('2023:06:15', format="%Y:%m:%d")
xxx = pd.to_datetime('2023년 06월 15일', format="%Y년 %m월 %d일")
xxx = pd.to_datetime('2023년 06월 15일 12:24:45', format="%Y년 %m월 %d일 %H:%M:%S")
print(xxx)

# 2. 연산 가능
xxx = pd.to_datetime('2023/6/15')
xx2 = pd.to_datetime('2023/1/15')
print(xxx-xx2) # 151 days 00:00:00

# 3. datetime을 지정된 범위에서 반환
# 가. start, end 명시
xxx = pd.date_range('2023/1/1', '2023/6/1') # 일 단위로 생성 ['2023-01-01'.....'2023-06-01']
                                            # 기본 값 : freq='D'
xxx = pd.date_range('2023/1/1', '2023/6/1', freq='M') # 월 단위로 생성
xxx = pd.date_range('2023/1/1', '2023/6/1', freq='2M') # 2개월 단위로 생성
print(xxx)

# 나. start + periods
xxx = pd.date_range('2023/1/1', periods = 5) #['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04','2023-01-05']
                                             # 기본 일단위. freq = "D"
xxx = pd.date_range('2023/1/1', periods = 5, freq = "M") # ['2023-01-31', '2023-02-28', '2023-03-31', '2023-04-30', '2023-05-31']
print(xxx)

# 활용
xxx = pd.date_range('2023/6/1',periods = 5)
df = pd.DataFrame({"시작가격":[500,200,50,240,455]
                   ,"종가":[1500,1200,150,1240,1455]},index = xxx)
print(df)

# 4. series --> datetime
df = pd.read_csv("./data/scientists.csv")
'''
                   Name        Born        Died  Age          Occupation
0     Rosaline Franklin  1920-07-25  1958-04-16   37             Chemist
1        William Gosset  1876-06-13  1937-10-16   61        Statistician
2  Florence Nightingale  1820-05-12  1910-08-13   90               Nurse
3           Marie Curie  1867-11-07  1934-07-04   66             Chemist
4         Rachel Carson  1907-05-27  1964-04-14   56           Biologist
5             John Snow  1813-03-15  1858-06-16   45           Physician
6           Alan Turing  1912-06-23  1954-06-07   41  Computer Scientist
7          Johann Gauss  1777-04-30  1855-02-23   77       Mathematician
'''
#print(df)
born = df['Born']
print(born) # dtype: object >> 문자열 출력
            # 연산이 불가능
born = pd.to_datetime(df['Born'])
print(born) #dtype: datetime64 >> 연산 가능

die = pd.to_datetime(df['Died'])
print(die)

df["생애"] = die - born
df["생애-년"] = die.dt.year - born.dt.year
print(df)

# 5. series.dt 속성 ==> series는 날짜타입인 경우 사용가능
xxx = pd.date_range('2023/1/1', periods = 5)
df = pd.DataFrame({"cur_date":xxx})
#print(dir(df['cur_date'].dt))
'''
'as_unit', 'ceil', 'date', 'day', 'day_name', 'day_of_week', 'day_of_year', 'dayofweek', 'dayofyear', 
'days_in_month', 'daysinmonth', 'floor', 'freq', 'hour', 'is_leap_year', 'is_month_end', 'is_month_start', 
'is_quarter_end', 'is_quarter_start', 'is_year_end', 'is_year_start', 'isocalendar', 'microsecond', 'minute', 
'month', 'month_name', 'nanosecond', 'normalize', 'quarter', 'round', 'second', 'strftime', 'time', 'timetz', 
'to_period', 'to_pydatetime', 'tz', 'tz_convert', 'tz_localize', 'unit', 'weekday', 'year'
'''

print("년도:", df['cur_date'].dt.year)
print("년도:", df['cur_date'].dt.month)
print("년도:", df['cur_date'].dt.day)


# 6. datetime -> str로 변경
print(df['cur_date'], df['cur_date'].astype(str))