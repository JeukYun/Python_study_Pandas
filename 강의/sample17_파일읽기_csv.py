import numpy as np
import pandas as pd
import seaborn as sns

from datetime import datetime
'''
    csv 파일읽기
    
    df = pd.read_csv(경로)

'''
import seaborn as sns

# 1. csv파일 읽기 기본
df = pd.read_csv("./data/scientists.csv")
print(df)
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

#2. 특정컬럼을 index로 변경
df = pd.read_csv("./data/scientists.csv", index_col=0) # 0번째 컬럼을 index로
print(df)

#3. 컬럼명 변경
df = pd.read_csv("./data/scientists.csv", header=0, names=['name', 'born', 'died', 'age', 'occupation'])
print(df)

# 4. 컬럼 선택 기본
df = pd.read_csv("./data/scientists.csv", usecols=['Age', 'Name']) # 지정 된 순서로 출력되지 않음 > 원본 순서로 출력.
print(df)

# 5. 지정된 갯수만 보기
df = pd.read_csv("./data/scientists.csv", nrows=3)
print(df)

# 6. , 아닌 임의의 구분자
df = pd.read_csv("./data/piped.csv", sep="|", index_col=0)
print(df)

# 7. csv파일로 저장
df.to_csv("./data/piped_copy.csv")
