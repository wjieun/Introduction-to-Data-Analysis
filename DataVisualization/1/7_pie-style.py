import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Apple SD Gothic Neo"

ratio = [34, 32, 16, 18]
labels = ['Apple', 'Banana', 'Melon', 'Grapes']
explode = [0.05, 0.05, 0.05, 0.05]
colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']

# autopct: 수치, 단위 출력
# explode: 파트끼리 띄우기
plt.pie(ratio, labels=labels, autopct='%.1f%%',
        explode=explode, shadow=True, colors=colors)
plt.show()