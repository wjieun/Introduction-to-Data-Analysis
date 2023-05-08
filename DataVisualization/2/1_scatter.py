import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")

X = df["PetalLength"]
Y = df["PetalWidth"]
plt.scatter(X, Y)
plt.show()