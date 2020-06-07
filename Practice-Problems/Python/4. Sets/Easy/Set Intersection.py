nE, englishRN, nF, frenchRN = int(input()), input().split(), int(input()), input().split()

englishRN, frenchRN = set(englishRN), set(frenchRN)

both = englishRN.intersection(frenchRN)

print(len(both))
