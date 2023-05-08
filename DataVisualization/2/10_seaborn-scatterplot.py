import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

sns.scatterplot(data=iris, x="petal_length", y="petal_width")
plt.show()

# hue: 색상을 이용하여 범주를 표현
sns.scatterplot(data=iris, x="petal_length", y="petal_width", hue="species")
plt.show()