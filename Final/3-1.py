# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

data_path = 'data/data_3.csv'


df = pd.read_csv(data_path)
mileage = df['Mileage']
engine = df['Engine']

m_Q1 = mileage.quantile(0.25)
m_Q3 = mileage.quantile(0.75)
m_IQR = m_Q3 - m_Q1
m_min = m_Q1 - 1.5 * m_IQR
m_max = m_Q3 + 1.5 * m_IQR

e_Q1 = engine.quantile(0.25)
e_Q3 = engine.quantile(0.75)
e_IQR = e_Q3 - e_Q1
e_min = e_Q1 - 1.5 * e_IQR
e_max = e_Q3 + 1.5 * e_IQR

def mileage_change(x):
	if x <= m_Q1: return m_min
	elif x >= m_Q3: return m_max
	else: return x

def engine_change(x):
	if x <= e_Q1: return e_min
	elif x >= e_Q3: return e_max
	else: return x

df['Mileage'] = df['Mileage'].apply(mileage_change)
df['Engine'] = df['Engine'].apply(engine_change)

corr_res = df.corr().loc['Price']
score_Mileage = corr_res['Mileage']
score_Engine = corr_res['Engine']
print( round(score_Mileage, 3), round(score_Engine, 3))