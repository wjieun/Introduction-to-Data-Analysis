import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.family"] = "Apple SD Gothic Neo"
plt.rcParams['axes.unicode_minus'] = False

X = np.random.randn(1000)
Y = np.random.randn(1000)
plt.title("Scatter Plot")
plt.scatter(X, Y)
plt.show()