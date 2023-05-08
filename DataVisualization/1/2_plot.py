import matplotlib.pyplot as plt
# 한글 폰트 설정
plt.rcParams["font.family"] = "Apple SD Gothic Neo"

# 그래프 제목 설정
plt.title("그래프 제목")

# 그래프 축 이름 설정
plt.xlabel("x축")
plt.ylabel("y축")

# 그래프 x축, y축 값 지정
plt.plot([10, 20, 30, 40], [1, 10, 100, 1000])
plt.show()