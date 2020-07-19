import numpy as np
dim = list(map(int, input().split()))
print(np.zeros(dim, dtype = np.int), np.ones(dim, dtype = np.int), sep="\n")