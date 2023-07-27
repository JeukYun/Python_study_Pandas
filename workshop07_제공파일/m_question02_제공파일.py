
import pandas as pd
import numpy as np

user_usage = pd.read_csv("./data/user_usage.csv")
user_device = pd.read_csv("./data/user_device.csv")
devices = pd.read_csv("./data/android_devices.csv")


### 코드 구현 ######
xxx = pd.merge(user_usage, user_device, how="left", on = "use_id")
print(xxx)

### 코드 구현 ######
