d = {}
for i in range(int(input())):
    data = input()
    d[data] = d.get(data,0) + 1
print(len(d),' '.join(map(str,d.values())),sep="\n")
