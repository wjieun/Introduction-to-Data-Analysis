import pandas as pd

names = ['춘향', '몽룡', '향단', '방자']
korean = [100, 95, 90, 85]
english = [85, 90, 95, 100]
math = [90, 85, 100, 95]

df = pd.DataFrame({'국어': korean, '영어': english, '수학': math}, index=names)
print(df)
print()

df.loc['학도'] = {'국어': 50, '영어': 50, '수학': 5} # 행 추가
print(df)
print()

# 행 삭제
# axis = 0: 행 방향, 1: 열 방향
# inplace = False(default): return, True: 현재 df에 반영
df.drop('학도', axis=0, inplace=True)
print(df)