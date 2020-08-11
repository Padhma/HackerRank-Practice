import re
for _ in range(int(input())):
    n = input()
    regex = '^[7-9]\d{9}$'
    if re.search(regex,n):
        print("YES")
    else:
        print("NO")