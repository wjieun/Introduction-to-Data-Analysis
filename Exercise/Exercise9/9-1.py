import matplotlib.pyplot as plt
import numpy as np
import os
os.makedirs('./data', exist_ok = True)

Semester = ['1-1','1-2','2-1','2-2','3-1','3-2','4-1','4-2']
Grade = [3.2,2.7,4.3,4.1,4.2,3.9,4.1,4.2]

fig_x = int(input())
fig_y = int(input())
fig = plt.figure(figsize=(fig_x, fig_y))

title = "Grade Graph"
plt.plot(Semester,Grade)
plt.title(title)

plt.savefig('./data/out.png')

fig.canvas.draw()
print(np.array(fig.canvas.renderer._renderer).sum(axis=(0, 1)))
