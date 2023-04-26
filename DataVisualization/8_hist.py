import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.family"] = "Apple SD Gothic Neo"
plt.rcParams['axes.unicode_minus'] = False

# 가우시안 표준 정규 분포 난수 1000개 생성
x = np.random.randn(1000)
plt.title("Histogram")

# bins: 막대의 너비
plt.hist(x, bins=100)
plt.show()