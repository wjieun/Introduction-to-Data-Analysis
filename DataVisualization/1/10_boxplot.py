import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.family"] = "Apple SD Gothic Neo"
plt.rcParams['axes.unicode_minus'] = False

data = np.random.randn(1000)

# 박스 아래: 25%(Q1), 가운데 주황 선: 50%(Q2), 박스 위: 75%(Q3)
# IQR(Inter Quartile Range) = Q3 - Q1
# 상단 수염(whisker) = Q3 + 1.5 * (IQR보다 작은 데이터 중 가장 큰 값)
# 하단 수염(whisker) = Q1 - 1.5 * (IQR보다 큰 데이터 중 가장 작은 값)
# 수염 표시를 경계로 이상치(outlier) 데이터를 구분
plt.boxplot(data)
plt.show()