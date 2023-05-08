import pandas as pd

df = pd.read_csv("iris.csv")
df2 = df.drop("caseno", axis=1)
gb = df2.groupby("Species").mean()

print(gb)
print()
print(gb.T)