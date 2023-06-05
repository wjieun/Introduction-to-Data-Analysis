# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import pandas as pd 

whr = pd.read_csv('data/WHR2022.csv')
data = whr.copy()
data = data.drop(['Whisker-high', 'Whisker-low'], axis=1)
data.columns = ['rank', 'country', 'happy_score', 'residual', 'gdp',
								 'social_support', 'health', 'freedom', 'generosity', 'trust']
data.drop(['rank', 'country'], axis=1, inplace=True)

nums = data.shape[0]
h_border = data.iloc[int(nums/3)]['happy_score']
m_border = data.iloc[int(nums/3)*2]['happy_score']

def encoding_group_rank(x):
    if x >= h_border: return 'H'
    elif x >= m_border: return 'M'
    else: return 'L'

data['group_rank'] = data['happy_score'].apply(encoding_group_rank)
gb = data.groupby('group_rank').mean().sort_values('happy_score', ascending=False)

HL = gb.loc['H'] / gb.loc['L']
print(HL.idxmax(), round(HL.max(), 4))

HL.drop([HL.idxmax()], inplace=True)
print(HL.idxmax(), round(HL.max(), 4))