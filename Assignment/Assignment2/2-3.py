import pandas as pd
import numpy as np

path = 'data/weather_perturbed_3.csv'
df = pd.read_csv(path)
df.fillna(method='ffill', inplace=True)
# 채점을 위한 코드입니다.
# 마지막 제출하는 데이터프레임의 이름을 df로 맞춰주세요.
idx = input()
print(df.iloc[int(idx)])