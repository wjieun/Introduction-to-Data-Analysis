# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import pandas as pd

Korean=[100, 90, 90, 95, 85, 80, 75, 80, 75, 70, 65, 65, 50, 40, 50, 50]
English=[100, 95, 95 ,90, 85, 80, 85, 70, 70, 60, 65, 55, 60, 60, 50, 50]
Math=[100, 90, 95, 85, 80, 70, 60, 70, 85, 80, 95, 45, 80, 85, 50, 75]
Science=[100, 90, 90, 85, 85, 95, 50, 70, 85, 70, 80, 30, 85, 75, 50, 85]
scores = pd.DataFrame( {'korean':Korean,'english':English, 'math':Math, 'science':Science} )

a = input()
b = input()

corr_res = scores.corr()
print(corr_res.loc[a][b])