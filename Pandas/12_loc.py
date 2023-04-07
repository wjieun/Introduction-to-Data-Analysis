# 레이블 기반의 2차원 인덱싱
import pandas as pd

names = ['춘향', '몽룡', '향단', '방자']
korean = [100, 95, 90, 85]
english = [85, 90, 95, 100]
math = [90, 85, 100, 95]

df = pd.DataFrame({'국어': korean, '영어': english, '수학': math}, index=names)
print(df)
print()

# 행 접근
print(df.loc['춘향'])
print()

# 행 리스트 접근
print(df.loc[['춘향', '향단']])
print()

# 개별 값 접근
# 아래 두 형태 모두 가능
print(df.loc['춘향', '국어'])
print(df.loc['춘향']['국어'])
print()

# 행 슬라이싱 접근
# 주의!! 슬라이스의 마지막 값이 포함됨
print(df.loc['몽룡':'방자'])
print()

# 불리언 시리즈 접근
print(df.loc[df['국어'] > 90])
print()

# 행 & 열 모두 리스트로 접근
print(df.loc[['춘향', '몽룡'], ['수학', '영어']])
print()

# 수학 90점 넘는 학생의 국어 & 영어 점수
print(df.loc[df['수학'] > 90, ['국어', '영어']])