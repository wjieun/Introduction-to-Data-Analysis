import pandas as pd

names = ['춘향', '몽룡', '향단', '방자']
korean = [100, 95, 90, 85]
english = [85, 90, 95, 100]
math = [90, 85, 100, 95]

df = pd.DataFrame({'이름': names, '국어': korean, '영어': english, '수학': math})
print(type(df))
print(df)

print(df.columns)
print(df.index)
print()

name_ser = df['이름']
print(type(name_ser))
print(name_ser) 