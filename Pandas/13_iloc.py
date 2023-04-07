# 순서를 나타내는 정수 기반의 2차원 인덱싱
import pandas as pd

names = ['춘향', '몽룡', '향단', '방자']
korean = [100, 95, 90, 85]
english = [85, 90, 95, 100]
math = [90, 85, 100, 95]

df = pd.DataFrame({'국어': korean, '영어': english, '수학': math}, index=names)
print(df)
print()

print(df.iloc[0]) # 한 행 접근
print(df.iloc[[0, 2]]) # 여러 행 접근
print(df.iloc[0, 0]) # 단일 값 접근
print()

print(df.iloc[0:2]) # 행 슬라이싱
print()

print(df.iloc[0:2, 1:3]) # 행&열 슬라이싱
print()

print(df.iloc[[0, 3], [1, 2]]) # 행&열 리스트 접근
print()

print(df.iloc[0] > 90) # 불리언 시리즈
print()

# 행렬 인덱스 0의 학생 점수 중 90점이 넘는 과목
print(df.iloc[0][df.iloc[0] > 90])