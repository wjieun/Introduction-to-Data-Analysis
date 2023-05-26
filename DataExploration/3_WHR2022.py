import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

whr = pd.read_csv('WHR2022.csv')
data = whr.copy()
print(data.info(), '\n')

data2 = data.drop(['Whisker-high', 'Whisker-low'], axis=1) # 불필요 항목 제거
# 컬럼 이름 간단하게 변경
data2.columns = ['rank', 'country', 'happy_score', 'residual', 'gdp',
                 'social_support', 'health', 'freedom', 'generosity', 'trust']
print(data2, '\n')
print(data2.duplicated().sum(), '\n') # 중복 데이터 체크
print(data2.isnull().sum(), '\n') # 결측 데이터 체크

# 행복지수 값으로 정렬
data3 = data2.sort_values('happy_score', ascending=False)
print(data3.head(10), '\n') # 행복지수 상위 10개국
print(data3.tail(10), '\n') # 행복지수 하위 10개국

data3.drop(['rank', 'country'], axis=1, inplace=True)
print(data3.head(10).mean(), '\n')
print(data3.tail(10).mean(), '\n')
print(data3.head(10).mean() / data3.tail(10).mean(), '\n')

sns.pairplot(data3)
plt.show()

# for c in data3.columns:
#     plt.figure(figsize=(4, 3))
#     sns.boxplot(x=c, data=data3)
#     plt.show()

plt.figure(figsize=(30, 3))
i = 1
for c in data3.columns:
    plt.subplot(1, len(data3.columns), i)
    sns.boxplot(x=c, data=data3)
    i += 1
plt.show()

plt.figure(figsize=(30, 3))
i = 1
for c in data3.columns:
    if c != 'happy_score':
        plt.subplot(1, len(data3.columns)-1, i)
        i += 1
        sns.scatterplot(x=c, y='happy_score', data=data3)
plt.show()

corr_res = data3.corr()
print(corr_res, '\n')
plt.figure(figsize=(10, 8))
sns.heatmap(corr_res, annot=True, cmap='YlGnBu')
plt.show()

print(corr_res.loc['happy_score'], '\n')
corr_res.loc['happy_score'].plot.bar()
plt.show()

nums = data3.shape[0]
h_border = data3.iloc[int(nums/3)]['happy_score']
m_border = data3.iloc[int(nums/3)*2]['happy_score']
print(h_border, m_border, '\n')

def encoding_group_rank(x):
    if x >= h_border: return 'H'
    elif x >= m_border: return 'M'
    else: return 'L'

data3['group_rank'] = data3['happy_score'].apply(encoding_group_rank)
print(data3, '\n')

print(data3.groupby('group_rank').mean().sort_values('happy_score', ascending=False))

sns.scatterplot(x='freedom', y='gdp', hue='group_rank', data=data3)
plt.show()

sns.scatterplot(x='generosity', y='gdp', hue='group_rank', data=data3)
plt.show()