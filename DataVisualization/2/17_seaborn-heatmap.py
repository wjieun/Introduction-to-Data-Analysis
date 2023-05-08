import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")
pvt = flights.pivot("month", "year", "passengers")
print(pvt)
plt.figure(figsize=(10, 6))
# annot: 숫자 표시, fmt: 숫자 포맷, cmap: 색상
sns.heatmap(pvt, annot=True, fmt="d", cmap="YlGnBu")
plt.show()