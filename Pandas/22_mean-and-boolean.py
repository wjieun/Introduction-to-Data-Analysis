import pandas as pd
df = pd.read_csv("iris.csv")

print(df.count())
print()

# FutureWarning: Automatic reindexing on DataFrame vs Series comparisons is deprecated and will raise ValueError in a future version.
# 데이터프레임과 시리즈를 비교하는 과정이기에 Warning이 뜨지만 해결책은 따로 없어 보임
print(df > df.mean(numeric_only=True))
print()

df2 = df[df > df.mean(numeric_only=True)]
print(df2)
print()

print(df2.count())