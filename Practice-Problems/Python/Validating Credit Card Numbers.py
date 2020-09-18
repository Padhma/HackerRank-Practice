import re

for _ in range(int(input())):
    card = input()
    if re.match(r"[456][\d]{3}(-?\d{4})(-?\d{4})(-?)\d{4}$", card):
        if re.search(r"([\d])\1\1\1", card.replace("-","")):
            print('Invalid')
        else:
            print('Valid')
    else:
        print('Invalid')