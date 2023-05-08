# bar horizontal
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Apple SD Gothic Neo"

menu = ['아메리카노', '카페라테', '마키아또']
sales = [25, 35, 15]

plt.title("Bar Chart")
plt.xlabel("판매수")
plt.ylabel("메뉴")

# 수평 막대 그래프: 인자 순서 주의
plt.barh(menu, sales)
plt.show()