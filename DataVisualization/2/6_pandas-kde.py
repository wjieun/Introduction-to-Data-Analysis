import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")
df2 = df.drop("caseno", axis=1)
df2.plot.kde()
plt.show()