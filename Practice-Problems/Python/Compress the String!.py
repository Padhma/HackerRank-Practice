from itertools import groupby

# an_iterator = itertools.groupby(input(), lambda x : x[0]) 
# string_tuple = []
# for key, group in an_iterator: 
#     group_count = len(list(group))
#     string_tuple.append( "({}, {})".format(group_count,key) )

# print(" ".join(string_tuple))

print(*[(len(list(group)), int(key)) for key,group in groupby(input())]) 
