from sklearn.datasets import load_boston
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

boston = load_boston()
print(boston.keys())
print(type(boston.data))
print(type(boston.target))

dataset = pd.DataFrame(boston.data, columns=boston.feature_names)
dataset['mid_price'] = boston.target
print(dataset)
print(dataset.info())
print(dataset.duplicated().sum())
print(dataset.isna().sum())

plt.figure(figsize=(80, 4))
i = 1
for c in dataset.columns:
    if c != 'mid_price':
        plt.subplot(1, len(dataset.columns)-1, i)
        i += 1
        sns.scatterplot(x=c, y='mid_price', data=dataset)
plt.show()

res = dataset.corr()
print(res.loc['mid_price'], '\n')
res.loc['mid_price'].plot.bar()
plt.show()