import pandas as pd
file_path = 'data/score_1.csv' # 파일 경로
pd.set_option('mode.chained_assignment',  None)
score_1 = pd.read_csv(file_path)

print('원본 점수표')
print(score_1)

##여기에 코드를 작성하세요##
print("과락 반영 점수표")
score_1.drop(score_1[score_1['역사'] < 60].index, inplace=True)
print(score_1)

#########################