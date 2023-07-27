import numpy as np
import pandas as pd
import seaborn as sns

from datetime import datetime
###########################################
### 4.  df.groupby 이용
###########################################
'''
    https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html

    #1. 기본
      df.groupby('그룹으로 묶을 컬럼명')[선택컬럼].그룹함수
      예> emp.groupby(by = "deptno")["sal"].sum()
      
    #2. apply, agg, aggregate 함수
      df.groupby('그룹으로 묶을 컬럼명')[선택컬럼].agg(함수명)
      df.groupby('그룹으로 묶을 컬럼명')[선택컬럼].agg([함수명,함수명2, .....함수명])
    
    #3. 여러 컬럼에 다양한 함수 적용
      df.groupby('그룹으로 묶을 컬럼명').agg({
      컬럼명1 : [그룹함수, 그룹함수]
      컬럼명2 : [그룹함수, 그룹함수]
      })

'''
import seaborn as sns

department = {"deptno":[10,20,30,40],'dname':['개발','인사','영업','관리'],'loc':['서울','부산','제주','광주']}
employee = {"empno":['A1','A2','A3','A4','A5'],"ename":['홍길동','유관순','안중근','강감찬','이순신'],
            "sal":[1000,1500,2300,3400,4500],"hireday":['2019/01/02','2018/01/02','2017/01/02','2016/01/02','2015/01/02'],
            "deptno":[10,20,10,30,10]}
department_df = pd.DataFrame(department)
employee_df = pd.DataFrame(employee)

dept = pd.DataFrame(department)
emp = pd.DataFrame(employee)

print(dept)
'''
   deptno dname loc
0      10    개발  서울
1      20    인사  부산
2      30    영업  제주
3      40    관리  광주
'''
print(emp)
'''
  empno ename   sal     hireday  deptno
0    A1   홍길동  1000  2019/01/02      10
1    A2   유관순  1500  2018/01/02      20
2    A3   안중근  2300  2017/01/02      10
3    A4   강감찬  3400  2016/01/02      30
4    A5   이순신  4500  2015/01/02      10
'''

# 1. 부서별 sal 합, 평균
xxx = emp.groupby(by = "deptno")["sal"].sum() # by = 은 생략해도 무관
xxx2 = emp.groupby(by = "deptno")["sal"].mean() # by = 은 생략해도 무관
# min, max, count 등 가능
# ==시리즈 형태로 출력
print(xxx)
'''
deptno
10    7800
20    1500
30    3400
'''
print(xxx2)
'''
deptno
10    2600.0
20    1500.0
30    3400.0
'''

# 2. apply 또는 agg함수
def my_mean(v):
    print(">>", v) # deptno 별 sal 값 전달됨
    n = len(v)
    sum = 0
    for k in v:
        sum+=k
    return sum/n

#아래 세가지 결과는 동일
xxx3 = emp.groupby(by = "deptno")["sal"].agg(my_mean) # xxx3 = emp.groupby(by = "deptno")["sal"].mean() 과 동일
xxx3 = emp.groupby(by = "deptno")["sal"].agg(np.mean) # numpy의 그룹함수
xxx3 = emp.groupby(by = "deptno")["sal"].agg("mean") # python의 그룹함수
print(xxx3)

# 3. apply 또는 agg함수 적용 - 멀티함수
xxx4 = emp.groupby(by = "deptno")["sal"].agg([np.sum, np.mean, np.max, np.min, np.size])
xxx4 = emp.groupby(by = "deptno")["sal"].agg([sum, "mean", max, min, "count"])
                                             # sum, min, max 은 파이썬의 builtin 함수이므로 "" 생략이 가능하다
print(xxx4)

# 4. 여러 컬럼에 다양한 함수 적용
xxx5 = emp.groupby(by = "deptno").agg({
    "sal":["sum","max","min"],
    "deptno":["count"]
})
print(xxx5)