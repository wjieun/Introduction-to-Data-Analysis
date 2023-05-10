import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.random.randn(1000)
ol_data = pd.Series(data.copy())
ol_num = 10
for i in range(ol_num):
    rand_id = np.random.randint(0, len(data))
    ol_data[rand_id] = ol_data[rand_id] * 5

Q1 = ol_data.quantile(0.25)
Q3 = ol_data.quantile(0.75)
IQR = Q3 - Q1

idx1 = ol_data[ol_data > (Q3 + 1.5 * IQR)].index
idx2 = ol_data[ol_data < (Q1 - 1.5 * IQR)].index

ol_data.drop(idx1, inplace=True)
ol_data.drop(idx2, inplace=True)

print(ol_data.count())
plt.figure(figsize=(16, 8))
plt.boxplot(ol_data)
plt.show()