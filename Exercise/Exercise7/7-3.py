import pandas as pd
import numpy as np
file_path = 'data/score_3.csv' # 파일 경로
score_3 = pd.read_csv(file_path)

file_path_grades = 'data/grades.csv'
grades = pd.read_csv(file_path_grades)

pd.set_option('mode.chained_assignment',  None)
##여기에 코드를 작성하세요##
score_result = pd.merge(grades, score_3)
print("학점이 기재된 점수표")
print(score_result)

grades_result = score_result.groupby("학점")
print("학점 별 평균 점수")
print(grades_result.mean())
#########################