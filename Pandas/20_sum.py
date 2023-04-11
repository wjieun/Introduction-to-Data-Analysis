import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(10, size=(3, 6)))
print(df)
print()

# default: axis=0
# column에 대하여 행 방향으로 합산
print(df.sum())
print()

print(df.sum(axis=1))
print()

# 행과 열에 각 합계 결과를 추가
df['RowSum'] = df.sum(axis=1)
df.loc['ColSum'] = df.sum(axis=0)
print(df)