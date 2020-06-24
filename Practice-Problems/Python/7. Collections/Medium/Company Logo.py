from collections import Counter
s = sorted(input())
c = Counter(s).most_common(3)
for x in range(3):
    print(c[x][0], c[x][1])