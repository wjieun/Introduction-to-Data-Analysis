import pandas as pd
import numpy as np
file_path = 'data/score_4.csv' # 파일 경로
score_4 = pd.read_csv(file_path)

file_path_attend = 'data/attend.csv'
attend = pd.read_csv(file_path_attend)

pd.set_option('mode.chained_assignment',  None)

##여기에 코드를 작성하세요##
score_result = pd.merge(score_4, attend)
sort_mean_result = score_result.sort_values("평균", ascending=False)

print("평균 점수 상위 3명의 출석율")
print(sort_mean_result[:3][["이름","출석율"]], '\n')

print("평균 점수 하위 3명의 출석율")
print(sort_mean_result[-3:][["이름","출석율"]], '\n')


sort_attend_result = score_result.sort_values("출석율", ascending=False)

print("출석율 상위 3명의 평균 점수")
print(sort_attend_result[:3][["이름","평균"]], '\n')

print("출석율 하위 3명의 평균 점수")
print(sort_attend_result[-3:][["이름","평균"]], '\n')
#########################