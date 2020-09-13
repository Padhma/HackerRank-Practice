import re
n, m = input().split()
stringlist, string = [], ""
for _ in range(int(n)):
    stringlist.append(input())
for x in zip(*stringlist):
    string += "".join(x)
print(re.sub(r'(?<=\w)([^\w]+)(?=\w)', ' ', string))
# (?<=\w) -> positive lookbehind assertion for alphanumeric characters
# ([^\w]+) -> more than 1 special characters
# (?=\w) -> lookahead for alphanumeric characters