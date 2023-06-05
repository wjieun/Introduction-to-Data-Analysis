import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

study_hour = [[2], [5], [1], [7], [3], [4], [17], [6], [8], [5]]
class_pass = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]

lr = LinearRegression()

train_X = study_hour
train_Y = class_pass

lr.fit(train_X, train_Y)
print(lr.score(train_X, train_Y))

pred_Y = lr.predict(train_X)
plt.scatter(train_X, train_Y, marker='s')
plt.scatter(train_X, pred_Y, color='red')
plt.show()

test_X = [[4.5], [5.5]]
pred_Y = lr.predict(test_X)
print(pred_Y, '\n')

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()

lr.fit(train_X, train_Y)
print(lr.score(train_X, train_Y))

pred_Y = lr.predict(train_X)
print(list(pred_Y))
print(train_Y)

pred_Y = lr.predict(test_X)
print(pred_Y)