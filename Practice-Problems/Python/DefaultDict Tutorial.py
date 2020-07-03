from collections import defaultdict
n, m = map(int, input().split())
dd = defaultdict(list)
l = []
for i in range(n):
    dd[input()].append(i+1)
for j in range(m):
    l.append(input())
for i in l:
    if i in dd:
        print(' '.join(map(str,dd[i])))
    else:
        print("-1")