import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Apple SD Gothic Neo"
plt.rcParams['axes.unicode_minus'] = False

bill_length=[39.1, 39.5, 40.3, 36.7, 39.3, 38.9, 39.2, 34.1, 42.0, 37.8, 37.8, 41.1, 38.6, 34.6, 36.6, 38.7, 42.5, 34.4, 46.0, 37.8]
bill_depth=[18.7, 17.4, 18.0, 19.3, 20.6, 17.8, 19.6, 18.1, 20.2, 17.1, 17.3, 17.6, 21.2, 21.1, 17.8, 19.0, 20.7, 18.4, 21.5, 18.3]
body_mass=[3.75, 3.80, 3.25, 3.45, 3.65, 3.63, 4.68, 3.48, 4.25, 3.30, 3.70, 3.20, 3.80, 4.40, 3.70, 3.45, 4.50, 3.33, 4.20, 3.40]

plt.scatter(bill_length, bill_depth) # 펭귄 부리 길이와 두께
plt.show()

plt.scatter(bill_length, bill_depth, c=body_mass) # 컬러로 펭귄 몸무게를 함께 표현
plt.colorbar()
plt.show()