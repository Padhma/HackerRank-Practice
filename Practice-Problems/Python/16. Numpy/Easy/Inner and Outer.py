import numpy as np
array_A = list(map(int, input().split()))
array_B = list(map(int, input().split()))
print(np.inner(array_A,array_B), np.outer(array_A,array_B), sep="\n")