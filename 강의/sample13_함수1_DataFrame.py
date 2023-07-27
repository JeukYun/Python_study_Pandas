# print(dir(df))
'''
'T','abs', 'add', 'add_prefix', 'add_suffix', 'agg', 'aggregate', 'align', 'all', 'any', 'apply', 'applymap',
'asfreq', 'asof', 'assign', 'astype', 'at', 'at_time', 'attrs', 'axes', 'backfill', 'between_time',
'bfill', 'bool', 'boxplot', 'clip', 'col1', 'col2', 'col3', 'columns', 'combine', 'combine_first',
'compare', 'convert_dtypes', 'copy', 'corr', 'corrwith', 'count', 'cov', 'cummax', 'cummin', 'cumprod',
'cumsum', 'describe', 'diff', 'div', 'divide', 'dot', 'drop', 'drop_duplicates', 'droplevel', 'dropna',
'dtypes', 'duplicated', 'empty', 'eq', 'equals', 'eval', 'ewm', 'expanding', 'explode', 'ffill', 'fillna',
'filter', 'first', 'first_valid_index', 'flags', 'floordiv', 'from_dict', 'from_records', 'ge', 'get', 'groupby',
'gt', 'head', 'hist', 'iat', 'idxmax', 'idxmin', 'iloc', 'index', 'infer_objects', 'info', 'insert',
'interpolate', 'isetitem', 'isin', 'isna', 'isnull', 'items', 'iterrows', 'itertuples', 'join', 'keys',
'kurt', 'kurtosis', 'last', 'last_valid_index', 'le', 'loc', 'lt', 'mask', 'max', 'mean', 'median', 'melt',
'memory_usage', 'merge', 'min', 'mod', 'mode', 'mul', 'multiply', 'ndim', 'ne', 'nlargest', 'notna', 'notnull',
'nsmallest', 'nunique', 'pad', 'pct_change', 'pipe', 'pivot', 'pivot_table', 'plot', 'pop', 'pow', 'prod',
'product', 'quantile', 'query', 'radd', 'rank', 'rdiv', 'reindex', 'reindex_like', 'rename', 'rename_axis',
'reorder_levels', 'replace', 'resample', 'reset_index', 'rfloordiv', 'rmod', 'rmul', 'rolling', 'round',
'rpow', 'rsub', 'rtruediv', 'sample', 'select_dtypes', 'sem', 'set_axis', 'set_flags', 'set_index', 'shape',
'shift', 'size', 'skew', 'sort_index', 'sort_values', 'squeeze', 'stack', 'std', 'style', 'sub', 'subtract',
'sum', 'swapaxes', 'swaplevel', 'tail', 'take', 'to_clipboard', 'to_csv', 'to_dict', 'to_excel', 'to_feather',
'to_gbq', 'to_hdf', 'to_html', 'to_json', 'to_latex', 'to_markdown', 'to_numpy', 'to_orc', 'to_parquet',
'to_period', 'to_pickle', 'to_records', 'to_sql', 'to_stata', 'to_string', 'to_timestamp', 'to_xarray',
'to_xml', 'transform', 'transpose', 'truediv', 'truncate', 'tz_convert', 'tz_localize', 'unstack', 'update',
'value_counts', 'values', 'var', 'where', 'xs'
'''
## 2. DataFrame의 기술통계관련 함수
'''
  1. 최대(소)값         ==>  df.max(), df.min()
     누적최대(소)값,     ==>  df.cummax(), df.cummin()
      최대(소)값label   ==>  df.idxmax(), df.idxmin()
  2. (누적)합계         ==>  df.sum(), df.cumsum()
      평균              ==>  df.mean()
      중앙값            ==>  df.median()
      (누적)곱          ==>  df.prod(), df.cumprod()
  3. 사분위             ==>  df.quantile()
     분산               ==>  df.var()
      표준편차           ==>  df.std()
  4. count(갯수)         ==>  df.count()
  5. 통합 통계           ==>  df.describe()

'''

import pandas as pd
import numpy as np
import seaborn as sns

df = pd.DataFrame({"col1" : [4 ,6, 9, 5, 15],
                   "col2" : [16, 8, np.nan, 6, 6],
                   "col3" : [10, 11, 12, 12, 12]},
                    index = list("ABCDE"))
'''
    col1  col2  col3
A     4  16.0    10
B     6   8.0    11
C     9   NaN    12
D     5   6.0    12
E    15   6.0    12
'''
print(df)
# 1. 행을 축으로 최대/최소값 구하기 (컬럼별)
x = df.max(axis=0) # axis=0  위/아래,  axis=1 왼쪽/오른쪽
x = df.min(axis=0) # axis=0  위/아래,  axis=1 왼쪽/오른쪽
print(x)

# 2. 컬럼을 축으로 최대/최소값 구하기 (행별)
x = df.max(axis=1) #  axis=1 왼쪽/오른쪽
x = df.min(axis=1) #  axis=1 왼쪽/오른쪽
print(x)

# 3. 행을 축으로 누적최대/누적최소 구하기 (컬럼별)
x = df.cummax(axis=0)
x = df.cummin(axis=0)
print(x)

# 3. 컬럼을 축으로 누적최대/누적최소 구하기 (행별)
x = df.cummax(axis=1)
# x = df.cummin(axis=1)
print(x)

# 4. 행을 축으로 최대/최소값 라벨(인덱스라벨) 구하기 (컬럼별)
x = df.idxmax(axis=0)
x = df.idxmin(axis=0)
print(x)

# 4. 컬럼을 축으로 최대/최소값 라벨(컬럼명) 구하기 (행별)
x = df.idxmax(axis=1)
# x = df.idxmin(axis=1)
print(x)

# 5. 행을 축으로 총합/누적총합 구하기 (컬럼별) -  중요
x = df.sum(axis=0)
x = df.cumsum(axis=0)
print(x)

# 5. 컬럼을 축으로 총합/누적총합 구하기 (행럼별) -  중요
x = df.sum(axis=1)
x = df.cumsum(axis=1)
print(x)

# 6. 행/컬럼을 축으로 평균 구하기
x = df.mean(axis=0)
x = df.mean(axis=1)
print(x)

# 7. 행/컬럼을 축으로 중앙값 구하기
x = df.median(axis=0)
# x = df.median(axis=1)
print(x)

# 8. 행/컬럼을 축으로 곱연산 구하기
x = df.prod(axis=0)
# x = df.prod(axis=1)
print(x)

# 9. 행/컬럼을 축으로 분산 구하기
x = df.var(axis=0)
# x = df.var(axis=1)
print(x)

# 10. 행/컬럼을 축으로 표준편차 구하기
x = df.std(axis=0)
# x = df.std(axis=1)
print(x)

# 11. 행/컬럼을 축으로 갯수 구하기 ( 기본적으로 null 제외 )
x = df.count(axis=0)
# x = df.count(axis=1)
print(x)

# 12. 통합 통계 데이터
x = df.describe()
x = df.info() # SQL의 desc 테이블명과 비슷
print(x)
print(df.head()) # 상위 5개 출력
