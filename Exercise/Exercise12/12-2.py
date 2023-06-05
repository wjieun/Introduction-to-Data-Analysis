# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import pandas as pd 

whr = pd.read_csv('data/WHR2022.csv')
data = whr.copy()
data = data.drop(['Whisker-high', 'Whisker-low'], axis=1)
data.columns = ['rank', 'country', 'happy_score', 'residual', 'gdp',
								 'social_support', 'health', 'freedom', 'generosity', 'trust']
print(data.duplicated().sum())
print(data.isnull().sum())
data.info()