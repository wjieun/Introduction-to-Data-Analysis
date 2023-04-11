import pandas as pd

names = ['춘향', '몽룡', '향단', '방자']
korean = [100, 95, 90, 85]
english = [85, 90, 95, 100]
math = [90, 85, 100, 95]

df = pd.DataFrame({'국어': korean, '영어': english, '수학': math}, index=names)
print(df)
print()

df['체육'] = [100, 100, 100, 100] # 열 추가
print(df)
print()

# 열 삭제
# axis = 0: 행 방향, 1: 열 방향
# inplace = False(default): return, True: 현재 df에 반영
df.drop('체육', axis=1, inplace=True)
print(df)