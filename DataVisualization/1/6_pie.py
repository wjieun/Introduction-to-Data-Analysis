import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Apple SD Gothic Neo"

ratio = [34, 32, 16, 18]
labels = ['Apple', 'Banana', 'Melon', 'Grapes']

plt.pie(ratio, labels=labels)
plt.show()