import pandas as pd
file_name = 'data/data_3.csv'
data = pd.read_csv(file_name)
result = data[data['양성 여부'] == '양성']
print(len(result['양성 여부']))