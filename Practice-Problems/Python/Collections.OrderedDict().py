from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    item, _, price = input().rpartition(' ')
    d[item] = d.get(item, 0) + int(price)
print("\n".join(['{} {}'.format(k,v) for k,v in d.items()]))