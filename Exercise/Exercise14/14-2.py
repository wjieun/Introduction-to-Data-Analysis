import pandas as pd

df = pd.read_csv('data/winequality-red-converted.csv',dtype=float) # quality가 0 1로 변경된 데이터입니다.
df_test = df[:300]
df = df[300:]

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(max_iter=1000)
x = df.drop(['quality'], axis=1)
y = df['quality']
lr.fit(x, y)

test_x = df_test.drop(['quality'], axis=1)
test_y = df_test['quality']
train_score = lr.score(x, y)
test_score = lr.score(test_x,test_y)
train_pass = False
test_pass = False

if(train_score >= 0.7):
	train_pass = True


if(test_score >= 0.7):
	test_pass = True
print(train_pass,test_pass)