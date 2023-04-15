import pandas as pd
file_path = 'data/data_after_2.csv' #파일 경로

##여기에 코드를 작성하세요##
df = pd.read_csv(file_path)
df = df[(df['국어'] > 90) & (df['영어'] > 90) & (df['수학'] > 90)]




########################

print(df)



