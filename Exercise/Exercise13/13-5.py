# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from sklearn.datasets import load_boston
import pandas as pd

boston = load_boston()

dataset = pd.DataFrame(boston.data, columns=boston.feature_names)
dataset['mid_price'] = boston.target

test_set = dataset.iloc[:100]
train_set = dataset.iloc[100:]
train_X = train_set.drop(['mid_price'], axis=1)
train_Y = train_set['mid_price']
test_X = test_set.drop(['mid_price'], axis=1)
test_Y = test_set['mid_price']

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(train_X, train_Y)

coef = pd.Series(data=lr.coef_, index=train_X.columns) * 1000
coef = coef.sort_values(ascending=False)
print(coef)

print(round(lr.score(train_X, train_Y), 4))
print(round(lr.score(test_X, test_Y), 4))
print()

coef = coef.apply(abs).sort_values(ascending=True)
dataset2 = dataset.drop(coef.index[:5], axis=1)
test_set = dataset2.iloc[:100]
train_set = dataset2.iloc[100:]
train_X = train_set.drop(['mid_price'], axis=1)
train_Y = train_set['mid_price']
test_X = test_set.drop(['mid_price'], axis=1)
test_Y = test_set['mid_price']
lr.fit(train_X, train_Y)

print(round(lr.score(train_X, train_Y), 4))
print(round(lr.score(test_X, test_Y), 4))
print()


dataset3 = dataset.drop(['ZN', 'NOX'], axis=1)
test_set = dataset3.iloc[:100]
train_set = dataset3.iloc[100:]
train_X = train_set.drop(['mid_price'], axis=1)
train_Y = train_set['mid_price']
test_X = test_set.drop(['mid_price'], axis=1)
test_Y = test_set['mid_price']
lr.fit(train_X, train_Y)

print(round(lr.score(train_X, train_Y), 4))
print(round(lr.score(test_X, test_Y), 4))