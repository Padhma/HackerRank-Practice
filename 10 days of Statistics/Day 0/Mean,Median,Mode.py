# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
array = [int(n) for n in input().split()]

import numpy as np
from scipy import stats

#mean
mean = np.mean(array)
print(mean)

#median
median = np.median(array)
print(median)

#mode
mode = int(stats.mode(array)[0])
print(mode)
