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

# 1. python의 문자열 함수
print(dir(str))
'''
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 
'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 
'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 
'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 
'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 
'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 
'translate', 'upper', 'zfill'
'''

# 2. numpy의 문자열 함수
print(dir(np.char))
'''
'add', 'array', 'array_function_dispatch', 'asarray', 'asbytes', 'bool_', 
'capitalize', 'center', 'character', 'chararray', 'compare_chararrays', 'count',
'decode', 'encode', 'endswith', 'equal', 'expandtabs', 'find', 'functools', 
'greater', 'greater_equal', 'index', 'int_', 'integer', 'isalnum', 'isalpha', 
'isdecimal', 'isdigit', 'islower', 'isnumeric', 'isspace', 'istitle', 'isupper', 
'join', 'less', 'less_equal', 'ljust', 'lower', 'lstrip', 'mod', 'multiply', 
'narray', 'ndarray', 'not_equal', 'numpy', 'object_', 'overrides', 'partition', 
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 
'set_module', 'split', 'splitlines', 'startswith', 'str_len', 'string_', 'strip', 
'swapcase', 'title', 'translate', 'unicode_', 'upper', 'zfill'
'''

# 3. pandas의 문자열 함수
print(dir(Serise.str))
'''
'add', 'array', 'array_function_dispatch', 'asarray', 'asbytes', 'bool_', 
'capitalize', 'center', 'character', 'chararray', 'compare_chararrays', 'count', 
'decode', 'encode', 'endswith', 'equal', 'expandtabs', 'find', 'functools', 
'greater', 'greater_equal', 'index', 'int_', 'integer', 'isalnum', 'isalpha', 
'isdecimal', 'isdigit', 'islower', 'isnumeric', 'isspace', 'istitle', 'isupper', 
'join', 'less', 'less_equal', 'ljust', 'lower', 'lstrip', 'mod', 'multiply', 
'narray', 'ndarray', 'not_equal', 'numpy', 'object_', 'overrides', 'partition', 
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 
'set_module', 'split', 'splitlines', 'startswith', 'str_len', 'string_', 'strip', 
'swapcase', 'title', 'translate', 'unicode_', 'upper', 'zfill'
'''