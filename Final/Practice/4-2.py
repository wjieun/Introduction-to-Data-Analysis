import pandas as pd

df = pd.read_csv('22_fall_final_train.csv')

df = df.drop(['new_snowfall_3hr', 'cloud_type', 'lowest_cloud', 'ground_condition', 'wind_direction'], axis=1)
df = df.fillna(0)


def date_time_split(data):
    if isinstance(data, pd.core.frame.DataFrame):
        month_data = data.date_time.str[5:7].astype('int32')
    if isinstance(data, str):
        month_data = int(data[5:7])
    return month_data

A = int(input())
B = int(input())

df['month'] = df['date_time'].apply(date_time_split)
df2 = df[df['month'] == A]
gb = df2.groupby('station_name')
res = gb['activity_score'].mean().sort_values(ascending=False)
print(res.index[B-1])