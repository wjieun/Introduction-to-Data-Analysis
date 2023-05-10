import seaborn as sns
import matplotlib.pyplot as plt

def encoding(x):
    if x == 'male': return 0
    else: return 1

titanic = sns.load_dataset('titanic')
print(titanic, '\n')
print(titanic.count(), '\n')

titanic.count().plot.bar()
plt.show()

dup = titanic.duplicated()
print(dup.sum(), '\n')

titanic.drop_duplicates(inplace=True)
print(titanic.count(), '\n')

data = titanic.copy()
data = data[["survived", "sex", "fare", "age"]]
print(data.count(), '\n')
print(data.isna().sum(), '\n')
data.dropna(inplace=True)
print(data.count())

sns.boxplot(data=data) # 성별은 숫자가 아니라서 출력되지 않음
plt.show()

fare = data["fare"]
Q1 = fare.quantile(0.25)
Q3 = fare.quantile(0.75)
IQR = Q3 - Q1
print(Q1, Q3, IQR)
idx = fare[fare > (Q3 + 1.5 * IQR)].index
print(fare[idx].sort_values(ascending=False), '\n')

data['sex_code'] = data['sex'].apply(encoding) # 성별을 0과 1로 변환
data.reset_index(drop=True, inplace=True)
print(data)