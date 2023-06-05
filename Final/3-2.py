# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

data_path = 'data/data_4.csv'


df = pd.read_csv(data_path)
df['new'] = df['Engine'] / df['Seats']
col = input()
corr_res = df.corr().loc['new']
score = corr_res[col]
round_score = round(score, 3)
print(round_score)