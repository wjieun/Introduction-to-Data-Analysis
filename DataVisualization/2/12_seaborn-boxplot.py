import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

sns.boxplot(data=iris)
plt.show()

sns.boxplot(data=iris, x="species", y="petal_width")
plt.show()