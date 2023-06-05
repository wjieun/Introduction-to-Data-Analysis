import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
titanic = sns.load_dataset('titanic')
print(titanic)

dataset = titanic.copy()
dataset.drop(['class', 'who', 'deck', 'embark_town', 'alive'], axis=1, inplace=True)
dataset.drop_duplicates(inplace=True)
dataset.info()

def encoding_sex(x):
    if x == 'male': return 0
    else: return 1

def encoding_embarked(x):
    if x == 'S': return 0
    elif x == 'C': return 1
    else: return 2

def encoding_adult_male(x):
    if x == True: return 1
    else: return 0

def encoding_alone(x):
    if x == True: return 1
    else: return 0

dataset['sex'] = dataset['sex'].apply(encoding_sex)
dataset['embarked'] = dataset['embarked'].apply(encoding_embarked)
dataset['alone'] = dataset['alone'].apply(encoding_alone)
dataset['adult_male'] = dataset['adult_male'].apply(encoding_adult_male)

trainset = dataset.iloc[150:].copy()
testset = dataset.iloc[:150].copy()

trainset.dropna(inplace=True)
testset.dropna(inplace=True)

res = trainset.corr()
print(res)

plt.figure(figsize=(10, 8))
sns.heatmap(res, annot=True, cmap='YlGnBu')
plt.show()

# histplot은 겹쳐지는 부분의 가독성이 낮음
# for c in trainset.columns:
#     if c != 'survived':
#         sns.histplot(x=c, hue='survived', data=trainset)
#         plt.show()

# displot은 범주별로 그래프를 생성
# for c in trainset.columns:
#     if c != 'survived':
#         sns.displot(x=c, col='survived', hue='survived', data=trainset)
#         plt.show()

from sklearn.linear_model import LogisticRegression

# ConvergenceWarning: 모델이 충분히 학습되지 못함
# max_iter=300: 모델 최대 학습 횟수를 기본값 100에서 300으로 변경
lr = LogisticRegression(max_iter=300)

train_X = trainset.drop(['survived'], axis=1)
train_Y = trainset['survived']
test_X = testset.drop(['survived'], axis=1)
test_Y = testset['survived']

lr.fit(train_X, train_Y)
print(lr.score(train_X, train_Y))
print(lr.score(test_X, test_Y), '\n')

# 학습된 모델 계수(기울기) 값을 확인: 2차원 배열
print(lr.coef_)
coeff = pd.Series(data=lr.coef_[0], index=train_X.columns)
print(coeff.sort_values(ascending=False))


# age 값이 결측된 행을 모두 제거하는 대신 평균 값으로 대체
trainset = dataset.iloc[150:].copy()
trainset.fillna(trainset['age'].mean(), inplace=True)
columns = ['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'adult_male']

train_X = trainset[columns]
train_Y = trainset['survived']

# testset은 결측치가 제거된 버전을 사용
test_X = testset[columns]
test_Y = testset['survived']

lr.fit(train_X, train_Y)
print(lr.score(train_X, train_Y))
print(lr.score(test_X, test_Y))
