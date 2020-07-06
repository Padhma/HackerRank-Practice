n, m = map(int, input().split())
table = []
for _ in range(n):
    table.append(list(map(int,input().split())))
k = int(input())
for t in sorted(table, key = lambda x:x[k]):
    print(" ".join(map(str,t)))