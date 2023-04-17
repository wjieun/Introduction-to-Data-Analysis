# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import warnings
warnings.filterwarnings(action='ignore')
import numpy as np
import pandas as pd

# 데이터프레임 읽어오기
transaction_df = pd.read_csv("data/transactions.csv", index_col="일시")

# 기간 입력받기
start_date = input()
end_date = input()

# 주어진 기간으로 데이터프레임 자르기
transaction_df = transaction_df.loc[start_date:end_date]
date = transaction_df.groupby('시간')
c = date.count()
result = c['요일'].sort_values(ascending=False)
print(result.index[0])