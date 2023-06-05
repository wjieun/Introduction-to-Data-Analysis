import pandas as pd

df = pd.read_csv('22_fall_final_train.csv')

df = df.drop(['new_snowfall_3hr', 'cloud_type', 'lowest_cloud', 'ground_condition', 'wind_direction'], axis=1)
df = df.fillna(0)

def sign(x):
    if x > 0: return 1
    elif x == 0: return 0
    else: return -1

temp = df['temperature'] - 15
df['derivated_temp'] = abs(temp)
df['derivated_solar'] = temp.apply(sign) * df['solar_radiation']
print(round(df.corr()['temperature']['derivated_temp'], 2))
print(round(df.corr()['temperature']['derivated_solar'], 2))