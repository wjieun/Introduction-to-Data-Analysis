import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.family"] = "Apple SD Gothic Neo"
plt.rcParams['axes.unicode_minus'] = False

# plt.subplot(row, column, index)
plt.subplot(2, 2, 1)
plt.title("data1")
plt.plot(np.random.rand(5))

plt.subplot(2, 2, 2)
plt.title("data2")
plt.plot(np.random.rand(5))

plt.subplot(2, 2, 3)
plt.title("data3")
plt.plot(np.random.rand(5))

plt.subplot(2, 2, 4)
plt.title("data4")
plt.plot(np.random.rand(5))

# subplot 겹치지 않도록 최소한의 여백을 만들어 줌
plt.tight_layout()
plt.show()