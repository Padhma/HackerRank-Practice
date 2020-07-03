import itertools
n, l = int(input()), list(input().split())
k = int(input())
combi = list(itertools.combinations(l,k))
combi_filter = filter(lambda x: 'a' in x,combi)
print(len(list(combi_filter))/len(list(combi)))