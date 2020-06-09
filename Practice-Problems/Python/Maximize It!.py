from itertools import product
k, m = map(int,input().split())
l = ([int(x) for x in input().split()][1:] for _ in range(k))
# for _ in range(k):
#     l.append(set([int(x) for x in input().split()][1:]))
result = map(lambda x: sum(i**2 for i in x) % m, product(*l))
print(max(result))