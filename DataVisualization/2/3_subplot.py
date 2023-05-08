import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")

Y1 = df["SepalLength"]
Y2 = df["SepalWidth"]
Y3 = df["PetalLength"]
Y4 = df["PetalWidth"]

plt.subplot(2, 2, 1)
plt.hist(Y1)
plt.title("SepalLength")

plt.subplot(2, 2, 2)
plt.hist(Y2)
plt.title("SepalWidth")

plt.subplot(2, 2, 3)
plt.hist(Y3)
plt.title("PetalLength")

plt.subplot(2, 2, 4)
plt.hist(Y4)
plt.title("PetalWidth")

plt.tight_layout()
plt.show()