import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

# 그리드 형태로 각 데이터 열의 조합에 대해 scatter plot
# 같은 데이터가 만나는 대각선 영역에는 해당 데이터의 histogram
sns.pairplot(data=iris)
plt.show()

sns.pairplot(data=iris, hue="species")
plt.show()