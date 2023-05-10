import pandas as pd

dict_1 = {
    'item_id': [1, 1, 2, 2, 2, 2, 3, 4],
    'company': ['A', 'A', 'B', 'B', 'B', 'C', 'A', 'C'],
    'item_name': ['apple', 'apple', 'banana', 'banana', 'banana', 'banana', 'grape', 'watermelon'],
    'price': [15000, 15000, 4750, 4750, 4750, 4200, 13000, 18000],
    'color': ['red', 'red', 'yellow', 'yellow', 'yellow', 'yellow', 'purple', 'green']
}

df_1 = pd.DataFrame(dict_1)
print(df_1, '\n')

duplicated_bool = df_1.duplicated()
print(duplicated_bool, '\n')

df_1.drop_duplicates(inplace=True)
print(df_1, '\n')

print(df_1.loc[6], '\n')
print(df_1.iloc[3], '\n')

df_1.reset_index(inplace=True, drop=True)
print(df_1)
