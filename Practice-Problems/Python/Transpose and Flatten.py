import numpy as np
n, m = map(int, input().split())
array_A = np.array([input().split() for _ in range(n)], int)
print(np.transpose(array_A), array_A.flatten(), sep="\n")