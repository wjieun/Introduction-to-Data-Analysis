# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

data_path = 'data/data_2_1.csv'
company_data_path = 'data/company_data.csv'


df1 = pd.read_csv(data_path)
df2 = pd.read_csv(company_data_path)
df1 = df1.merge(df2)
gb = df1.groupby('Company_Name')
des = gb.describe()[('Year', 'count')]

company_name = input()
print(int(des[company_name]))