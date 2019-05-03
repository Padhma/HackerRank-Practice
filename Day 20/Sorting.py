#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

numberOfSwaps = 0
for j in range(n-1,0,-1):
    for i in range(j):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            numberOfSwaps += 1

print('Array is sorted in {0} swaps.'.format(numberOfSwaps))
print('First Element:',a[i])
print('Last Element:',a[n-1])


