import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

sns.jointplot(data=iris, x="sepal_length", y="sepal_width")
plt.show()

sns.jointplot(data=iris, x="sepal_length", y="sepal_width", hue="species")
plt.show()