import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.zeros(6).reshape(3, 2),
                   index=['a', 'b', 'c'],
                   columns=['v1', 'v2'])

df2 = pd.DataFrame(np.ones(4).reshape(2, 2),
                   index=['a', 'c'],
                   columns=['v1', 'v2'])
print(df1)
print()
print(df2)
print()
print(pd.concat([df1, df2], axis=0)) # 행 방향으로 합치기
print()
print(pd.concat([df1, df2], axis=1)) # 열 방향으로 합치기