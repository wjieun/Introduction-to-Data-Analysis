import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.family"] = "Apple SD Gothic Neo"
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(2, 2, 1)
ratio = [34, 32, 16, 18]
labels = ['Apple', 'Banana', 'Melon', 'Grapes']
explode = [0.05, 0.05, 0.05, 0.05]
colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
plt.pie(ratio, labels=labels, autopct='%.1f%%', explode=explode, shadow=True, colors=colors)
plt.title("data1")

plt.subplot(2, 2, 2)
menu = ['아메리카노', '카페라테', '마키아또']
sales = [25, 35, 15]
plt.title("Bar Chart")
plt.xlabel("판매수")
plt.ylabel("메뉴")
plt.barh(menu, sales)
plt.title("data2")

plt.subplot(2, 2, 3)
x = np.random.randn(1000)
plt.title("Histogram")
plt.hist(x, bins=100)
plt.title("data3")

plt.subplot(2, 2, 4)
data = np.random.randn(1000)
data_b = np.random.normal(-3.0, 1.5, 1000)
data_c = np.random.normal(1.2, 1.5, 1000)
plt.boxplot([data, data_b, data_c])
plt.xticks([1, 2, 3], ["데이터1", "데이터2", "데이터3"])
plt.title("data4")

plt.tight_layout()
plt.show()