import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Apple SD Gothic Neo"

plt.title("그래프 제목")

# 스타일: red(r), square(s), 점선(--)
plt.plot([10, 20, 30, 40], [1, 10, 100, 1000], 'rs--')
plt.xlabel("x축")
plt.ylabel("y축")
plt.show()