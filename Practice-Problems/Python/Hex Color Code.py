import re
for _ in range(int(input())):
    codematch = re.findall(r'.(#[0-9A-Fa-f]{6}|#[0-9A-Fa-f]{3})', input())
	# #[0-9A-Fa-f]{6} -> match valid hex color codes with 6 digits
	# #[0-9A-Fa-f]{3} -> match valid hex color codes with 3 digits
	# | -> match contains  either 6 or 3 digits
	# . -> any character
    if codematch:
        print(*codematch, sep="\n")