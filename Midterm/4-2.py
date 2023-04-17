# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import warnings
warnings.filterwarnings(action='ignore')
##채점을 위한 코드 입니다. 수정하지 않는 것을 권장합니다.
import pandas as pd
df_name = input()
menu_name = input()
df = pd.read_csv(df_name)
menu = pd.read_csv(menu_name)
ingredients_cost = {"cutlet" : 2500, "udon" : 1500, "shrimp_tempura" : 3000, "croquettes" : 2000}
################################################
total_list = []
igrd_list = []
for i in range(len(df['date'])):
	total = 0
	igrd_cost = 0
	for j in range(1, len(df.loc[i])):
		total += df.iloc[i, j] * menu.iloc[0, j]
		
		if j == 1 or j == 5 or j == 7:
			igrd_cost += df.iloc[i, j] * ingredients_cost["cutlet"]
		if j == 2 or j == 5:
			igrd_cost += df.iloc[i, j] * ingredients_cost["udon"]
		if j == 3 or j == 6 or j == 7:
			igrd_cost += df.iloc[i, j] * ingredients_cost["shrimp_tempura"]
		if j == 4 or j == 6 or j == 7:
			igrd_cost += df.iloc[i, j] * ingredients_cost["croquettes"]
		
	total_list.append(total)
	igrd_list.append(igrd_cost)
	
df['Total_price'] = total_list
df['Total_ingredients_cost'] = igrd_list
df['Profit'] = df['Total_price'] - df['Total_ingredients_cost']

print(df[['date', 'Total_price', 'Total_ingredients_cost', 'Profit']])

#다음은 각 테스트 케이스별 판매 목록 csv 파일 경로입니다.
#data/2023_midterm_4_1_0.csv
#data/2023_midterm_4_1_1.csv
#data/2023_midterm_4_1_2.csv

#다음은 각 테스트 케이스별 판매 메뉴 csv 파일 경로입니다.
#data/2023_midterm_4_menu_0.csv
#data/2023_midterm_4_menu_1.csv