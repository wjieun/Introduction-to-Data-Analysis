import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

sns.histplot(data=iris, x="petal_length", bins=10)
plt.show()

sns.histplot(data=iris, x="petal_length", bins=10, hue="species")
plt.show()