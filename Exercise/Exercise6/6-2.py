import pandas as pd
file_path = 'data/data.csv' # 파일 경로

##여기에 코드를 작성하세요##
df = pd.read_csv(file_path)
end = len(df) - 9
df = df.loc[7:end]
df = df.loc[:, df.columns != '성별']





########################

print(df)



