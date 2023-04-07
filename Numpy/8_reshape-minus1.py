import numpy as np
arr = np.arange(12)
# 행은 상관 없고 열을 2열로 맞추고 싶을 때
arr2 = arr.reshape(-1, 2)
print(arr2)