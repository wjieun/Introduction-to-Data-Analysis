import numpy as np
import pandas as pd
df = pd.read_csv("iris.csv")
# numeric_only를 지정해 주지 않으면 숫자가 아닌 값으로 인해 Warning이 뜸
# 기본적으로 숫자가 아닌 값들은 빼고 계산하기는 함
print(df.mean(numeric_only=True))
print()
print(df['SepalLength'].mean())