#!/bin/python3

import math
import os
import random
import re
import sys

N = int(input())

if N%2 == 0:
    if 2 < N < 5:
        print("Not Weird")
    if 6 < N <= 20:
        print("Weird")
    if N>20:
        print("Not Weird")
else:
    print("Weird")
    
    
