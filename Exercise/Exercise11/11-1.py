import pandas as pd
import numpy as np

# Seaborn 라이브러리에서 제공하는 타이타닉 데이터 입니다.
titanic = pd.read_csv('data/Q0.csv')

def encoding(x):
	if x == 'male': return 0
	else: return 1

data = titanic.copy()
data = data[["survived", "sex", "fare", "age", "embarked"]]
data.drop_duplicates(inplace=True)
data.dropna(inplace=True)
data['sex_code'] = data['sex'].apply(encoding)
data.reset_index(drop=True, inplace=True)
print(data)