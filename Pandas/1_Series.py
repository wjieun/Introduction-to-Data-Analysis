import pandas as pd
grades = ['A', 'B+', 'A+', 'A']
ser = pd.Series(grades, index=['춘향', '몽룡', '향단', '방자'])
print(type(ser))
print(ser)
print()
print(ser[0], ser[2])
print(ser['춘향'], ser['향단'])
print(ser.index)