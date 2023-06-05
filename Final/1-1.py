# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

data_path = 'data/data_1_1.csv'

df = pd.read_csv(data_path)
df = df.drop(['New_Price'], axis=1)
a = int(input())
b = int(input())
print(df[a:b])