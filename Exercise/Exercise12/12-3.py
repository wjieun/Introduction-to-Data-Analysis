# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import pandas as pd 

whr = pd.read_csv('data/WHR2022.csv')
data = whr.copy()
data = data.drop(['Whisker-high', 'Whisker-low'], axis=1)
data.columns = ['rank', 'country', 'happy_score', 'residual', 'gdp',
								 'social_support', 'health', 'freedom', 'generosity', 'trust']
data.drop(['rank', 'country'], axis=1, inplace=True)

a = input()
corr_res = data.corr().loc[a].drop([a])
print(corr_res.idxmax(), round(corr_res.max(), 4))
print(corr_res.idxmin(), round(corr_res.min(), 4))