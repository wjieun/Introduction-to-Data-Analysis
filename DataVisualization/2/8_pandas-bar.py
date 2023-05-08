import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Apple SD Gothic Neo"

df = pd.read_csv("iris.csv")
df2 = df.drop("caseno", axis=1)
gb = df2.groupby("Species").mean()

gb.plot.bar(rot=0)
plt.title("각 종의 Feature별 평균")
plt.ylabel("평균")

gb.T.plot.bar(rot=0)
plt.title("각 종의 Feature별 평균")
plt.ylabel("평균")
plt.show()