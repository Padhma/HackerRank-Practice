#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    # 7*-9
    maxsum = -63
    for i in range(len(arr)-2):
        for j in range(len(arr[i])-2):
            hourglasssum = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            maxsum = hourglasssum if hourglasssum > maxsum else maxsum

    return maxsum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
