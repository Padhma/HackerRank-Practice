import numpy as np
np.set_printoptions(legacy='1.13')
r, c = map(int, input().split())
array = np.array([input().split() for _ in range(r)], int)
print(np.mean(array, axis=1), np.var(array, axis=0), np.std(array, axis=None), sep="\n")