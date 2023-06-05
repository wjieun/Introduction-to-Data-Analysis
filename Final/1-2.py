# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

data_path = 'data/data_1_2.csv'

df = pd.read_csv(data_path)
print(df.isna().sum())
df = df.dropna()
print(df.isna().sum())