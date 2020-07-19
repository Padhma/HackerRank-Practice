import numpy as np
n = int(input())
array_A = np.array([input().split() for _ in range(n)], float)
print(round(np.linalg.det(array_A),2))