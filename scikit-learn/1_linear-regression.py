from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

lr = LinearRegression()

X = [[163], [179], [166], [169], [171]]
Y = [54, 63, 57, 56, 58]

lr.fit(X, Y)
plt.scatter(X, Y, marker='s')
y_pred = lr.predict(X)
# plt.scatter(X, y_pred, color='red')
plt.plot(X, y_pred, 'r')
plt.show()