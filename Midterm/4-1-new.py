import pandas as pd

df_name = input()
menu_name = input()
df = pd.read_csv(df_name)
menu = pd.read_csv(menu_name)

df_v = df.iloc[:, 1:].values
menu_v = menu.iloc[:, 1:].values
df['Total_price'] = (df_v * menu_v).sum(axis=1)

print(df[['date', 'Total_price']])