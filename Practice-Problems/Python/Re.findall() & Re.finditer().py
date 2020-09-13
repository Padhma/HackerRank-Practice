import re
match = re.findall(r'[^aeiou]([aeiouAEIOU]{2,})(?=[^aeiou])', input())
# [^aeiou] -> find consonants 
# ([aeiouAEIOU]{2,}) -> fnd vowels between consonants repeating more than twice
# (?=[^aeiou]) -> find consonants and allow next search for vowels
if len(match)==0:
    print(-1)
else:
    print(*match, sep="\n")