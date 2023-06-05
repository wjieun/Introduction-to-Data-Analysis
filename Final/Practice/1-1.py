import pandas as pd

df = pd.read_csv('22_fall_final_train.csv')

df = df.drop(['new_snowfall_3hr', 'cloud_type', 'lowest_cloud', 'ground_condition', 'wind_direction'], axis=1)
print(df.columns)