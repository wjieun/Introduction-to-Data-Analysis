import numpy as np
arr = np.arange(20).reshape(4, 5)
print(arr)
print(arr[0])
print(arr[0][1:3])
print(arr[2][1])
print()
print(arr[2, 1])
print(arr[[0, 2], [1, 3]])