import pandas as pd

df_name = input()
menu_name = input()
df = pd.read_csv(df_name)
menu = pd.read_csv(menu_name)
igrd = {"cutlet" : 2500, "udon" : 1500, "shrimp_tempura" : 3000, "croquettes" : 2000}

igrd["A_set"] = igrd["cutlet"] + igrd["udon"]
igrd["B_set"] = igrd["shrimp_tempura"] + igrd["croquettes"]
igrd["Special_set"] = igrd["cutlet"] + igrd["shrimp_tempura"] + igrd["croquettes"]

df_v = df.iloc[:, 1:].values
menu_v = menu.iloc[:, 1:].values
igrd_v = pd.DataFrame(igrd, index=[0]).values

df['Total_price'] = (df_v * menu_v).sum(axis=1)
df['Total_ingredients_cost'] = (df_v * igrd_v).sum(axis=1)
df['Profit'] = df['Total_price'] - df['Total_ingredients_cost']

print(df[['date', 'Total_price', 'Total_ingredients_cost', 'Profit']])