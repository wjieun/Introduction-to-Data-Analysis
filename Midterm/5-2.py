# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import warnings
warnings.filterwarnings(action='ignore')
import numpy as np
import pandas as pd

# 데이터프레임 읽어오기
transaction_df = pd.read_csv("data/transactions.csv", index_col="일시")
name_df = pd.read_csv("data/account_names.csv")  # 계좌주 이름 데이터프레임
worktype_df = pd.read_csv("data/work_types.csv")  # 업종 데이터프레임

# 기간 입력받기
start_date = input()
end_date = input()

# 주어진 기간으로 데이터프레임 자르기
transaction_df = transaction_df.loc[start_date:end_date]
transaction_df['계좌번호'] = transaction_df['수신계좌번호']
df = pd.merge(transaction_df, name_df)
df = pd.merge(df, worktype_df)

gb = df.groupby('업종')
c = gb.sum()
result = c['송금액'].sort_values(ascending=False)
print(result.index[0])