import numpy as np
n, m, p = map(int, input().split())
matrix1 = np.array([input().split() for _ in range(n)], int)
matrix2 = np.array([input().split() for _ in range(m)], int)

print(np.concatenate((matrix1, matrix2), axis=0))
