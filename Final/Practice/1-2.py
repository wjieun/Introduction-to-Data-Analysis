import pandas as pd

df = pd.read_csv('22_fall_final_train.csv')

col = input()
df[col] = df[col].fillna(0)
print(round(df[col].mean(), 2))