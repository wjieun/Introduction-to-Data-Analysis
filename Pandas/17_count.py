import pandas as pd
df = pd.read_csv("iris.csv")
print(df.head())
print()
print(df['Species'])
print()
print(df['Species'].count())
print() 
print(df.count())