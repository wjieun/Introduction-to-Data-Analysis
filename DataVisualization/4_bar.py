import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Apple SD Gothic Neo"

menu = ['아메리카노', '카페라테', '마키아또']
sales = [25, 35, 15]

plt.title("Bar Chart")
plt.xlabel("메뉴")
plt.ylabel("판매수")

plt.bar(menu, sales)
plt.show()