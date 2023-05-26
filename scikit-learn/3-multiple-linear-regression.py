from sklearn.linear_model import LinearRegression

lr = LinearRegression()

X = [[171, 0], [169, 0], [176, 0], [168, 0], [181, 0], [166, 0], [180, 0], [175, 0],
     [163, 1], [162, 1], [171, 1], [162, 1], [164, 1], [162, 1], [158, 1], [173, 1]]

Y = [69, 65, 72, 67, 71, 65, 80, 71, 55, 51, 59, 53, 61, 56, 47, 57]

lr.fit(X, Y)
print(lr.score(X, Y))
print(lr.coef_)

test_X = [[168, 0], [168, 1]]
print(lr.predict(test_X))