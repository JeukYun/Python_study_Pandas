
import pandas as pd
import numpy as np

user_usage = pd.read_csv("./data/user_usage.csv")
user_device = pd.read_csv("./data/user_device.csv")
devices = pd.read_csv("./data/android_devices.csv")

#print("user_usage 데이터프레임: \n", user_usage)
#print("user_device 데이터프레임: \n",user_device)
#print("devices 데이터프레임: \n",devices)

result = pd.merge(user_usage, user_device, how="inner", on = "use_id")
### 코드 구현 ######
devices.rename(columns={"Retail Branding":"manufacturer"}, inplace=True)
#print(devices.head())



### 코드 구현 ######
print(result.head())

