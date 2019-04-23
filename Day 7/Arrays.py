#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    reverse = arr[::-1]

    #reversedArray = " ".join( str(a) for a in reverse )

    reversedArray = " ".join( map (str, reverse) )

    print(reversedArray)


