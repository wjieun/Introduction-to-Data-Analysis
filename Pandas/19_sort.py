import pandas as pd
df = pd.read_csv("iris.csv")

# 인덱스 값을 기준으로 정렬
# print(df['SepalLengthCm'].sort_index())

# 데이터 값을 기준으로 정렬
print(df['SepalLength'].sort_values()) # 시리즈 반환
print(df.sort_values('SepalLength')) # 데이터프레임 반환
print()

# sort_values([A, B])
# A열 기준으로 정렬 후 동일한 값이 나오면 B열 기준으로 정렬
print(df.sort_values(['SepalLength', 'SepalWidth']))