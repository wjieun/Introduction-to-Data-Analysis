import pandas as pd
file_path = 'data/data_after_2.csv' #파일 경로
pd.set_option('mode.chained_assignment',  None) # 입출력을 제어하기 위한 코드입니다.
##여기에 코드를 작성하세요##
df = pd.read_csv(file_path)
df['국어'] += 10
df['국어'][df['국어'] > 100] = 100


########################

print(df)



