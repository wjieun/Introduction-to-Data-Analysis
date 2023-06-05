# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import warnings
import pandas as pd
from sklearn.linear_model import LinearRegression
warnings.filterwarnings('ignore')

train_data_path = 'data/train_data_4.csv'
test_data_path = 'data/test_data_4.csv'

df_train = pd.read_csv(train_data_path)
df_test = pd.read_csv(test_data_path)

columns = ['Price', 'Name', 'Transmission', 'Company_Name']

train_data = df_train.drop(columns, axis=1)
train_label = df_train['Price']

test_data = df_test.drop(columns, axis=1)
test_label = df_test['Price']

lr = LinearRegression()
lr.fit(train_data, train_label)
answer_train_df = pd.read_csv('data/train_data_4.csv')
answer_test_df = pd.read_csv('data/test_data_4.csv')
cheating = False
if len(train_data) != len(answer_train_df) or len(test_data) != len(answer_test_df) :
	print("train, test length error")
if lr.score(train_data, train_label) >= 0.9 or lr.score(test_data, test_label) >= 0.9 :	
	print(f"Train Score: {lr.score(train_data, train_label):.4f}, Test Score: {lr.score(test_data, test_label):.4f}  -  Cheating")
if lr.score(train_data, train_label) >= 0.75 and lr.score(test_data, test_label) >= 0.75 :	
	print(f"Train Score: {lr.score(train_data, train_label):.4f}, Test Score: {lr.score(test_data, test_label):.4f}  -  Passed")
else :
	print(f"Train Score: {lr.score(train_data, train_label):.4f}, Test Score: {lr.score(test_data, test_label):.4f}  -  Failed")
