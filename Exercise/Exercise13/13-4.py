# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
data = [ [171,'male', 69], [169,'male', 65], [176,'male', 72], [168,'male', 67], [181,'male', 71], [166,'male', 65], [180,'male', 80], [175,'male', 71], [163,'female', 55], [162,'female', 51], [171,'female', 59], [162,'female', 53], [164,'female', 57], [162,'female', 56], [158,'female', 47], [173,'female', 57], [171,'unknown', 72], [169,'unknown', 66], [176,'unknown', 71], [168,'unknown', 69], [181,'unknown', 74]]
#반올림때 쓰는 round 함수 예시입니다.
#score = round(score, 4)
#반올림때 쓰는 round 함수 예시입니다.
#score = round(score, 4)
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.DataFrame(data, columns=['height', 'sex', 'weight'])
train_label = df['weight']
df = df.drop(['weight'], axis=1)

def sex_to_int1(x):
	if x == 'male': return 0
	elif x == 'female': return 1
	else: return 2

def sex_to_int2(x):
	if x == 'male': return 0
	elif x == 'female': return 1
	else: return 0

df1 = df.copy()
df1['sex'] = df1['sex'].apply(sex_to_int1)

df2 = df.copy()
df2['sex'] = df2['sex'].apply(sex_to_int2)

lr1 = LinearRegression()
lr1.fit(df1, train_label)
score1 = round(lr1.score(df1, train_label), 4)

lr2 = LinearRegression()
lr2.fit(df2, train_label)
score2 = round(lr2.score(df2, train_label), 4)

print(score1, score2)