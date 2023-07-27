
import pandas as pd
import numpy as np
pd.options.display.max_columns = 20
user_usage = pd.read_csv("./data/user_usage.csv")
user_device = pd.read_csv("./data/user_device.csv")
devices = pd.read_csv("./data/android_devices.csv")


### 코드 구현 ######
devices.rename(columns={"Retail Branding":"manufacturer"}, inplace=True)
print("user_usage \n", user_usage.columns)
print("user_device \n", user_device.columns)
print("devices \n", devices.columns)
x = pd.merge(user_usage, user_device, on = "use_id")
print(x.head(10))
print('----')
print(devices.head(10))





### 코드 구현 ######
