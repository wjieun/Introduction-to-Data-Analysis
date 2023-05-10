import pandas as pd

def process(x):
    if x >= 90: return 'A'
    elif x >= 80: return 'B'
    else: return 'C'

names = ['춘향', '몽룡', '향단', '방자']
math = [90, 85, 100, 95]
df = pd.DataFrame({'이름': names, '수학': math})
print(df, '\n')

tmp = df.copy()
tmp['수학'] = tmp['수학'].apply(process)
print(tmp, '\n')

df['학점'] = df['수학'].apply(process)
print(df)