import pandas as pd
import numpy as np

dict_1 = {
    'col1': [1, 2, 3, np.nan, np.nan],
    'col2': [10, 20, np.nan, 40, 50],
    'col3': [np.nan, 200, 300, 400, np.nan]
}

df_1 = pd.DataFrame(dict_1)
print(df_1, '\n')
print(pd.isna(df_1), '\n') # print(pd.isnull(df_1)

print(pd.isna(df_1).sum())
print(pd.isna(df_1).sum().sum(), '\n')

print(df_1.count())
print(df_1.count().sum(), '\n')

print(df_1.shape)
print(df_1.shape[0] * df_1.shape[1])