import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")

Y1 = df["SepalLength"]
Y2 = df["SepalWidth"]
Y3 = df["PetalLength"]
Y4 = df["PetalWidth"]

plt.hist(Y1, alpha=0.6, label="SepalLength")
plt.hist(Y2, alpha=0.6, label="SepalWidth")
plt.hist(Y3, alpha=0.6, label="PetalLength")
plt.hist(Y4, alpha=0.6, label="PetalWidth")
plt.legend()
plt.show()