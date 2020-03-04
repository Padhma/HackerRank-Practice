import re

for _ in range(int(input())):
    inputString = input()
    try:
        re.compile(inputString)
        print(True)
    except re.error:
        print(False)