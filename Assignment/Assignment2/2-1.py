import pandas as pd
path = 'data/weather_perturbed_1.csv'
df = pd.read_csv(path)

df.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True)


# 채점을 위한 코드입니다.

####################################################
# 데이터프레임을 제출할 때 이름을 df로 하셔야 채점됩니다 #
####################################################

idx = input()
print(df.iloc[int(idx)])