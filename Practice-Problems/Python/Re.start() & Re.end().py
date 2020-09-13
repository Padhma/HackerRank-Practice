import re
string = input()
substring = input()
stringlist = [(m.start(),m.start()+len(substring)-1) for m in re.finditer(r'(?={})'.format(substring),string)]
#  '(?={})'.format(substring) -> lookahead for the substring in the entire string
if len(stringlist)>0:
    for s in stringlist:
        print(s)
else:
    print('(-1, -1)')