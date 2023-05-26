from sklearn.datasets import load_boston
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
print(lr.score(train_X, train_Y))

pred = lr.predict(train_X)
sns.scatterplot(x=train_Y, y=pred)
plt.show()

print(lr.score(test_X, test_Y))
pred = lr.predict(test_X)
sns.scatterplot(x=test_Y, y=pred)
plt.show()

for i in range(len(train_X.columns)):
    print(train_X.columns[i], ":\t", lr.coef_[i] * 1000)
print()

coef = pd.Series(data=lr.coef_, index=train_X.columns) * 1000
print(coef.sort_values(ascending=False))