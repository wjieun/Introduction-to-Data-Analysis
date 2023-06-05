import pandas as pd
import numpy as np

# Seaborn 라이브러리에서 제공하는 타이타닉 데이터를 처리한 데이터입니다.
titanic = pd.read_csv('data/Q1.csv')

# 여기에서 데이터를 처리하세요
data = titanic.copy()
data['age'].fillna(data['age'].mean(), inplace=True)
vc = data['embarked'].value_counts().index[0]
data['embarked'].fillna(vc, inplace=True)

processed_data = data # 이 변수에 처리된 데이터를 저장하세요!

# 이 부분은 processed_data 변수를 이용해 출력값을 내는 부분입니다.
# 채점은 이 부분을 활용하여 진행되니 다른 출력값을 내지 마세요.

print(processed_data['age'].value_counts())
print(processed_data['embarked'].value_counts())