# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
test_set = [list(map(int, input().split())) for _ in range(5)]
test_label = list(map(int, input().split()))
#input에 의한 test set 정의입니다. 신경안쓰셔도 됩니다.
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
train_X = [[1], [0], [-2], [3], [-4], [5], [-6], [7], [-8]]
train_Y = [3, 2, 6, 11, 18, 27, 38, 51, 66]
lr.fit(train_X, train_Y)
pred = lr.predict(test_set)
print(pred)

intercept = round(lr.intercept_, 4)
print( lr.coef_, intercept)
score = round(lr.score(test_set, test_label), 4)
print(score)