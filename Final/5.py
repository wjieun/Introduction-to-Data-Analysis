# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import warnings
import pandas as pd
from sklearn.linear_model import LinearRegression
warnings.filterwarnings('ignore')

train_data_path = 'data/train_data_5.csv'
test_data_path = 'data/test_data_5.csv'
company_data_path = 'data/company_number.csv'

df_train = pd.read_csv(train_data_path)
df_test = pd.read_csv(test_data_path)
company_number_data = pd.read_csv(company_data_path)
company_number_data = company_number_data.set_index('Company_Name')

columns = ['Price', 'Name', 'Company_Name']
def transmission_value(x):
	if x == 'Manual': return 0
	elif x == 'Automatic': return 1
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

df_train['Transmission'] = df_train['Transmission'].apply(transmission_value)
df_test['Transmission'] = df_test['Transmission'].apply(transmission_value)
df_train['Location'] = df_train['Location'].apply(location_value)
df_test['Location'] = df_test['Location'].apply(location_value)
df_train['Fuel_Type'] = df_train['Fuel_Type'].apply(fuel_type_value)
df_test['Fuel_Type'] = df_test['Fuel_Type'].apply(fuel_type_value)
df_train['Owner_Type'] = df_train['Owner_Type'].apply(owner_type_value)
df_test['Owner_Type'] = df_test['Owner_Type'].apply(owner_type_value)

train_data = df_train.drop(columns, axis=1)
train_label = df_train['Price']

test_data = df_test.drop(columns, axis=1)
test_label = df_test['Price']

lr = LinearRegression()
lr.fit(train_data, train_label)
answer_train = pd.read_csv('data/train_data_5.csv')
answer_test = pd.read_csv('data/test_data_5.csv')
answer_company = pd.read_csv('data/company_number.csv')

answer_train_merge = pd.merge(answer_train, answer_company)
answer_test_merge = pd.merge(answer_test, answer_company)

if len(train_data) != len(answer_train) or len(test_data) != len(answer_test) :
	print("train, test length error")

empty = answer_train["Price"].compare(train_label).empty or answer_train_merge["Price"].compare(train_label).empty
if not empty :
	print("train label error")
	
empty = answer_test["Price"].compare(test_label).empty or answer_test_merge["Price"].compare(test_label).empty
if not empty :
	print("test label error")

target_score = float(input())
if lr.score(train_data, train_label) >= target_score and lr.score(test_data, test_label) >= target_score :
	print(f"Train Score: {lr.score(train_data, train_label):.4f}, Test Score: {lr.score(test_data, test_label):.4f}  -  Passed")
	if lr.score(train_data, train_label) >= 0.9 or lr.score(test_data, test_label) >= 0.9 :
		print("Cheating")
else :
	print(f"Train Score: {lr.score(train_data, train_label):.4f}, Test Score: {lr.score(test_data, test_label):.4f}  -  Failed")