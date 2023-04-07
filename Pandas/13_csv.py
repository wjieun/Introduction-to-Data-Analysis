import pandas as pd

df = pd.read_csv("iris.csv")
print(df)

print(df.head()) # 시작 다섯 행
print(df.head(10)) # 시작 열 행

print(df.tail()) # 끝 다섯 행
print(df.tail()) # 끝 열 행

print(df.index) # RangeIndex(start=0, stop=150, step=1)
print(df.columns) # Index([...])

# 열 기준으로 count(개수), mean(평균), std(표준편차), min(최소), max(최대),
# 상위 25%, 50%, 75% 값 출력
print(df.describe())

res = df.describe()
print(type(res))
print(res.loc['mean'])
print(res.loc['mean']['PetalWidth'])