nl, ml = input().split()
n = input().split()
setA = set(input().split())
setB = set(input().split())

happ = sum([(i in setA)-(i in setB) for i in n])
# for i in n:
#     if i in setA:
#         happ += 1
#     elif i in setB:
#         happ -= 1

print(happ)