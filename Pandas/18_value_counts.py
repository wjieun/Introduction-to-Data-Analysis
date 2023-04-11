import pandas as pd
df = pd.read_csv("iris.csv")
print(df['Species'].value_counts())
print()
print(df['SepalLength'].value_counts())