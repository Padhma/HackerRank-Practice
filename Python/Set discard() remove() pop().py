n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    try:
        operation, *num = input().split()
        getattr(s,operation)(*map(int,num))
    except KeyError:
        continue

print(sum(s))

