n = int(input())
roomNum = input().split()

set1 = set()
set2 = set()

for x in roomNum:
    if x in set1:
        set2.add(x)
    else:
        set1.add(x)
captainRoom = set1.difference(set2)
print(" ".join(captainRoom))