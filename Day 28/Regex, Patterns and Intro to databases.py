#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())

    names = list()

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        pattern = '.+@gmail.com$'

        result = re.match(pattern,emailID)

        if result:
            names.append(firstName)
    
    print('\n'.join(sorted(names)))
