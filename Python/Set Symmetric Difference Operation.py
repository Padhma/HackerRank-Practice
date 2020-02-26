nE, englishRN, nF, frenchRN = int(input()), input().split(), int(input()), input().split()

englishRN, frenchRN = set(englishRN), set(frenchRN)
sym_diff = englishRN.symmetric_difference(frenchRN)
print(len(list(sym_diff)))