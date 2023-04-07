import pandas as pd

names = ['춘향', '몽룡', '향단', '방자']
korean = [100, 95, 90, 85]
english = [85, 90, 95, 100]
math = [90, 85, 100, 95]

df = pd.DataFrame({'국어': korean, '영어': english, '수학': math}, index=names)

bool_index = df['수학'] > 90
print(bool_index)
print()
print(df[bool_index])
print()

bool_index = df > 90
print(bool_index)
print()
print(df[bool_index])