import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.family"] = "Apple SD Gothic Neo"
plt.rcParams['axes.unicode_minus'] = False

data = np.random.randn(1000)
data_b = np.random.normal(-3.0, 1.5, 1000)
data_c = np.random.normal(1.2, 1.5, 1000)

# 여러 데이터를 리스트로 전달
plt.boxplot([data, data_b, data_c])

# 각 데이터의 라벨 설정
plt.xticks([1, 2, 3], ["데이터1", "데이터2", "데이터3"])

plt.show()