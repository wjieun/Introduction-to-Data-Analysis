import pandas as pd

# 숫자로 라벨링
i = [1, 2, 3, 4]
korean = [100, 95, 90, 85]
english = [85, 90, 95, 100]
math = [90, 85, 100, 95]

df = pd.DataFrame({'국어': korean, '영어': english, '수학': math}, index=i)
print(type(df))

# 라벨이 숫자일 때 슬라이싱을 하면 라벨이 아니라 인덱스가 기준
print(df[1:3])