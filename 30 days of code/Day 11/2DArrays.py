#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    maxSum = -9643281928

    for i in range(len(arr)-2):
        for j in range(len(arr[i])-2):
            hourglassSum = sum([arr[i][j],arr[i][j+1],arr[i][j+2],arr[i+1][j+1],arr[i+2][j],arr[i+2][j+1],arr[i+2][j+2]])
            maxSum = max(hourglassSum,maxSum)
    
    print(maxSum)



