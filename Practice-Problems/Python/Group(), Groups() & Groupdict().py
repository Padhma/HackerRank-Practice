import re
m = re.search(r'([a-zA-Z0-9])\1+', input())
# \1+ more than one repeating character
print(m.group(1) if m else -1)
