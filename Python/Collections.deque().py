from collections import deque

d = deque()

for _ in range(int(input())):
    operation, *num = input().split()
    getattr(d, operation)(*num)

print(*d)
