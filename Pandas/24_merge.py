import pandas as pd

df1 = pd.DataFrame({
    '고객번호': [1001, 1002, 1003, 1004, 1005, 1006, 1007],
    '이름': ['둘리', '도우너', '또치', '길동', '희동', '마이콜', '영희']
}, columns=['고객번호', '이름'])

print(df1)

df2 = pd.DataFrame({
    '고객번호': [1001, 1001, 1005, 1006, 1008, 1001],
    '금액': [10000, 20000, 15000, 5000, 100000, 30000]
}, columns=['고객번호', '금액'])

print(df2)

df3 = pd.merge(df1, df2)
print(df3)

# outer 병합 방식은 열 값이 한쪽만 있어도 합쳐서 보여 줌
df4 = pd.merge(df1, df2, how='outer')
print(df4)