import numpy as np
arr = np.arange(20).reshape(4, 5)
print(arr)
print()

# 행 슬라이싱
print(arr[1:3])
print()

# 행과 열 슬라이싱
print(arr[1:3, 1:4])
print()

# 열만 슬라이싱
print(arr[:, 1:3])