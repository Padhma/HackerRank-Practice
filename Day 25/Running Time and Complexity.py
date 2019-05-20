from math import sqrt

t = int(input())

for i in range(0,t):
    n = int(input())
    flag = 0
    if n < 2:
        flag = 1
    else:
        for j in range(2,int(sqrt(n))+1):
            if n % j == 0:
                flag = 1
    if flag == 1:
        print('Not prime')
    else:
        print('Prime')
