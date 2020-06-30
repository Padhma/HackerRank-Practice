import numpy as np
r, c = map(int, input().split())
array = np.array([input().split() for _ in range(r)], int)
print(np.max(np.min(array,axis=1)))