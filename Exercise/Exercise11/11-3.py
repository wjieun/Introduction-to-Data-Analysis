import pandas as pd
import numpy as np

# Seaborn 라이브러리에서 제공하는 타이타닉 데이터를 처리한 데이터입니다.
titanic = pd.read_csv('data/Q2.csv')

data = titanic.copy()
fare = data['fare']
Q1 = fare.quantile(0.25)
Q3 = fare.quantile(0.75)
IQR = Q3 - Q1
print(fare[fare > (Q3 + 1.5 * IQR)].mean())