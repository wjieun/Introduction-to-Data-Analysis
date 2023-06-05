# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

data_path = 'data/data_2_3.csv'

#round_vlaue = round(value, 1)
df = pd.read_csv(data_path)
gb = df.groupby('Seats')
power_mean = gb.describe()[('Power', 'mean')]
power_mean = round(power_mean, 1)

def fill_zero(x):
	if x['Power'] == 0:
		x['Power'] = power_mean[x['Seats']]
	return x

df = df.apply(fill_zero, axis=1)
	
idx = int(input())
row = df.iloc[idx]
print(row[['Name', 'Power']])