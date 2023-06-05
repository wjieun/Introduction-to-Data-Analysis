import pandas as pd
import numpy as np

path = 'data/weather_perturbed_2.csv'
df = pd.read_csv(path)

idx1 = df[(df['humidity'] < 0) | (df['humidity'] > 100)].index
df.loc[idx1, 'humidity'] = np.nan

temp = df['temperature']
Q1 = temp.quantile(0.25)
Q3 = temp.quantile(0.75)
IQR = Q3 - Q1

idx2 = df[(temp < (Q1 - 1.5 * IQR)) | (temp > (Q3 + 1.5 * IQR))].index
df.loc[idx2, 'temperature'] = np.nan
# 채점을 위한 코드입니다.
# 마지막 제출하는 데이터프레임의 이름을 df로 맞춰주세요.
print(df.isna().sum())