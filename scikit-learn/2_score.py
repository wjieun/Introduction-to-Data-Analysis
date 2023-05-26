from sklearn.linear_model import LinearRegression

lr = LinearRegression()

X = [[163], [179], [166], [169], [171]]
Y = [54, 63, 57, 56, 58]

lr.fit(X, Y)
print(lr.score(X, Y))
print(lr.coef_, lr.intercept_) # 기울기, 절편