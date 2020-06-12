n, x = map(int, input().split())
marksheet = []
for _ in range(x):
    marksheet.append(map(float, input().split()))
print(*[(sum(i)/len(i)) for i in zip(*marksheet)], sep="\n")
