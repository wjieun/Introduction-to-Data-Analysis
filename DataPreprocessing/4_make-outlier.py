import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = np.random.randn(1000)
plt.figure(figsize=(16, 8))
plt.plot(data, 'o')
plt.show()

ol_data = pd.Series(data.copy())
ol_num = 10
for i in range(ol_num):
    rand_id = np.random.randint(0, len(data))
    ol_data[rand_id] = ol_data[rand_id] * 5

plt.figure(figsize=(16, 8))
plt.plot(ol_data, 'o-')
plt.show()