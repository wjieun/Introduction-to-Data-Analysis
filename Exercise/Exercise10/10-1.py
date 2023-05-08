import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
os.makedirs('./data', exist_ok = True)
fig_x = int(input())
fig_y = int(input())
fig = plt.figure(figsize=(fig_x, fig_y))
file_path = 'data/heiweimus.csv'
df = pd.read_csv(file_path)
plt.bar(df['weight'], df['muscle'])
plt.title('weight-muscle')

plt.savefig('./data/out.png')
fig.canvas.draw()
print(np.array(fig.canvas.renderer._renderer).sum(axis=(0, 1)))