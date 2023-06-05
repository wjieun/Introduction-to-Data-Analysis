# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

data_path = 'data/data_2_2.csv'


df = pd.read_csv(data_path)

def location_value(x):
	if x == 'Ahmedabad': return 0
	elif x == 'Bangalore': return 1
	elif x == 'Chennai': return 2
	elif x == 'Coimbatore': return 3
	elif x == 'Delhi': return 4
	elif x == 'Hyderabad': return 5
	elif x == 'Jaipur': return 6
	elif x == 'Kochi': return 7
	elif x == 'Kolkata': return 8
	elif x == 'Mumbai': return 9
	elif x == 'Pune': return 10

def fuel_type_value(x):
	if x == 'CNG': return 0
	elif x == 'Diesel': return 1
	elif x == 'LPG': return 2
	elif x == 'Petrol': return 3

def owner_type_value(x):
	if x == 'First': return 0
	elif x == 'Second': return 1
	elif x == 'Third': return 2
	else: return 3

df['Location'] = df['Location'].apply(location_value)
df['Fuel_Type'] = df['Fuel_Type'].apply(fuel_type_value)
df['Owner_Type'] = df['Owner_Type'].apply(owner_type_value)

idx = int(input())
row = df.iloc[idx]
print(row.loc[['Location', 'Fuel_Type', 'Owner_Type']])