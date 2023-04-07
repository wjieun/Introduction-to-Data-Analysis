import pandas as pd

names = ['춘향', '몽룡', '향단', '방자']
korean = [100, 95, 90, 85]
english = [85, 90, 95, 100]
math = [90, 85, 100, 95]

df = pd.DataFrame({'국어': korean, '영어': english, '수학': math}, index=names)
print(type(df))
print()

# 인덱스로 슬라이싱 하면 end의 전까지 출력
print(df[0:2])
print()

# 라벨로 슬라이싱 하면 end까지 출력
print(df['춘향':'향단'])