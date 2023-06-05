# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import matplotlib.pyplot as plt
img = plt.imread("data/skorea2.png")

plt.figure(figsize=(131.3 - 124.3, 38.7 - 32.8))
plt.tight_layout()
plt.xlim(124.3, 131.3)
plt.ylim(32.8, 38.7)
plt.imshow(img, aspect='auto', extent=[124.3, 131.3, 32.8, 38.7])
plt.grid()

# 데이터프레임 읽어온 후
# scatterplot 그리기, legend 표시하기
import pandas as pd
path = 'data/station.csv'
df = pd.read_csv(path)

plt.scatter(df['longitude'], df['latitude'], label='weather stations')
plt.legend()
plt.savefig('out.png')
plt.show()
answer_img = plt.imread('out.png')
print(answer_img.sum(axis=(0, 1)))