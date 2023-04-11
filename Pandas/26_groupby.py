import pandas as pd

data = {
    "도시": ["서울", "서울", "서울", "부산", "부산", "부산", "인천", "인천"],
    "연도": ["2015", "2010", "2005", "2015", "2010", "2005", "2015", "2010"],
    "인구": [9904312, 9631482, 9762546, 3448737, 3393191, 3512547, 2886172, 2660610],
    "지역": ["수도권", "수도권", "수도권", "경상권", "경상권", "경상권", "수도권", "수도권"]
}

columns = ["도시", "연도", "인구", "지역"]
df1 = pd.DataFrame(data, columns=columns)

gb = df1.groupby("도시")
print()

# 값이 숫자로 이루어진 열에 대해서만 계산
print(gb.mean())
print()

print(gb.sum())
print()

print(gb.count())
print()

des = gb.describe()
print(des)
print()

print(des.columns)
print()

print(des[('인구', 'mean')])