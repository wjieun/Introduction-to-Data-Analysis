import pandas as pd
import numpy as np
file_path = 'data/score_2.csv' # 파일 경로
score_2 = pd.read_csv(file_path)

file_path_additional = 'data/score_2_add.csv'
score_2_add = pd.read_csv(file_path_additional)

pd.set_option('mode.chained_assignment',  None)

print('과락 반영 점수표')
print(score_2)
print('전학생 시험 점수표')
print(score_2_add)

##여기에 코드를 작성하세요##
print("최종 점수표")
score_result = pd.concat([score_2, score_2_add])
score_result["평균"] = score_result.mean(axis=1, numeric_only=True)
print(score_result)
#########################