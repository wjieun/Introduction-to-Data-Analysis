import pandas as pd
file_name = 'data/data_3.csv'
data = pd.read_csv(file_name)
result = data[(data['연령'] >= 65) & (data['백신 접종 횟수'] >= 1) & (data['양성 여부'] == '양성')]
print(len(result['연령']))