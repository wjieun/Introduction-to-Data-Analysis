import pandas as pd

names = ['춘향', '몽룡', '향단', '방자']
korean = [100, 95, 90, 85]
english = [85, 90, 95, 100]
math = [90, 85, 100, 95]

df = pd.DataFrame({'이름': names, '국어': korean, '영어': english, '수학': math})
print(type(df))
print(df)
print()

print(df['국어'][1]) # 열 선택 후 행 인덱싱
print()
print(df[1:2]['국어']) # 행 선택 후 열 인덱싱
print()

res = df['국어'][1]
print(res)
print(type(res))
print()

res = df[1:2]['국어']
print(res)
print(type(res))