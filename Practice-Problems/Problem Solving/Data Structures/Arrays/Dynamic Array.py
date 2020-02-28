#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
   
    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    LastAnswer = 0
    seq = [[] for i in range(n)]

    for flag,x,y in queries:
        if flag == 1:
            index = (x ^ LastAnswer) % n
            seq[index].append(y)
        if flag == 2:
            index = (x ^ LastAnswer) % n
            size = len(seq[index])
            LastAnswer = seq[index][y % size] 
            print(LastAnswer)           


