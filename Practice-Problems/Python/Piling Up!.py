from collections import deque
for _ in range(int(input())):
    n, cubelist = int(input()), deque(map(int, input().split()))
    for i in range(n//2):
        if cubelist[0] < cubelist[1] and cubelist[-1] < cubelist[-2]:
            print("No")
            break
        cubelist.pop()
        cubelist.popleft()
        if len(cubelist) == 0 or len(cubelist) == 1:
            print("Yes")
            break