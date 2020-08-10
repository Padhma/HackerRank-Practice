import re
for _ in range(int(input())):
    f = input()
    if(re.search(r'^[-+]?[0-9]*\.[0-9]+$',f)):
        print('True')
    else:
        print('False')