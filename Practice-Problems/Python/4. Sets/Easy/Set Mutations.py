setAlen, setA = int(input()), input().split()
setA = set(setA)

for _ in range(int(input())):
    operation, num = input().split()
    newSet = input().split()
    getattr(setA, operation)(newSet)

print(sum( map(int, setA) ))

