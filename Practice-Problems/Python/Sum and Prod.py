import numpy as np
r, c = map(int, input().split())
array = np.array([input().split() for _ in range(c)], int)
print(np.prod(np.sum(array, axis=0)))