import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")

sns.lineplot(data=flights, x="year", y="passengers")
plt.show()

sns.lineplot(data=flights, x="year", y="passengers", hue="month")
plt.show()

sns.lineplot(data=flights, x="month", y="passengers")
plt.show()

sns.lineplot(data=flights, x="month", y="passengers", hue="month")
plt.show()

sns.boxplot(data=flights, x="year", y="passengers")
plt.show()

sns.boxplot(data=flights, x="month", y="passengers")
plt.show()