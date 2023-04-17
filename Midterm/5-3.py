# UTF-8 encoding when using korean
import warnings
warnings.filterwarnings(action='ignore')
import numpy as np
import pandas as pd

transaction_df = pd.read_csv("data/transactions.csv", index_col="일시")
name_df = pd.read_csv("data/account_names.csv")  # 계좌주 이름 데이터프레임
worktype_df = pd.read_csv("data/work_types.csv")  # 업종 데이터프레임

start_date = input()
end_date = input()

transaction_df = transaction_df.loc[start_date:end_date]

df1 = pd.merge(transaction_df, name_df, left_on='송신계좌번호', right_on='계좌번호')
df1 = pd.merge(df1, worktype_df)
df1 = df1[df1['업종'] == '개인']
df1 = df1.drop(['계좌번호', '이름', '업종'], axis=1)

df2 = pd.merge(df1, name_df, left_on='수신계좌번호', right_on='계좌번호')
df2 = pd.merge(df2, worktype_df)

gb = df2.groupby('업종')
c = gb.sum()
result = c['송금액'].sort_values(ascending=False)
print(result.index[0])