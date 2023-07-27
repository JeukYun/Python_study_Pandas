

import numpy as np
import pandas as pd

np.random.seed(123456)
df = pd.DataFrame({'foo':np.random.random(10000), 'key':range(100, 10100)})
print(df.head())
### 코드 구현 ######
df.set_index('key', inplace=True)
print(df.head())
print(df[:10099])

### 코드 구현 ######

