
import pandas as pd
import numpy as np

user_usage = pd.read_csv("./data/user_usage.csv")
user_device = pd.read_csv("./data/user_device.csv")
devices = pd.read_csv("./data/android_devices.csv")


### 코드 구현 ######
print(devices.columns)

print(devices[devices["Model"] == "SM-G930F"])

print(devices[devices["Device"].str.startswith('GT')])

### 코드 구현 ######

