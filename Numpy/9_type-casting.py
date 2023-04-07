import numpy as np
arr = np.arange(5)
print(arr[0], arr[1])
print()
arr[0] = 777
print(arr)

# 넘파이 배열 요소는 자료형이 같아야 함
# arr[1] = "hi"

# int형 배열에 float을 넣으면 int로 형변환됨
arr[1] = 3.14
print(arr)