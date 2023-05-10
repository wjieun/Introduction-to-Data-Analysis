import pandas as pd
import numpy as np

dict_1 = {
    'col1': [1, 2, 3, np.nan, np.nan],
    'col2': [10, 20, np.nan, 40, 50],
    'col3': [np.nan, 200, 300, 400, np.nan]
}

df_1 = pd.DataFrame(dict_1)
print(df_1, '\n')

df_2 = df_1.copy() # 원본을 수정하지 않기 위해
df_2.dropna(inplace=True)
print(df_2, '\n')

df_2 = df_1.copy()
df_2.fillna(0, inplace=True)
print(df_2, '\n')

df_2 = df_1.copy()
print(df_2.mean(), '\n')
df_2.fillna(df_2.mean(), inplace=True)
print(df_2, '\n')