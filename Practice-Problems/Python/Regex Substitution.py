import re

for _ in range(int(input())):
    print(re.sub(r"((?<=\s)\&\&\s)", "and ", re.sub(r"(\s\|\|\s)", " or ", input()))) 

# ((?<=\s)\&\&\s) -> ?<= is positive lookbehind to check for characters after space
# \&\&\s -> check for && followed by space
# (\s\|\|\s) -> check for space followed by || by space