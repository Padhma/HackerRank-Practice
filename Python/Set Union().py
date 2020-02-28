nE, englishRN, nF, frenchRN = int(input()), input().split(), int(input()), input().split()

englishRN, frenchRN = set(englishRN), set(frenchRN)
oneSubscription = englishRN | frenchRN
print(len(list(oneSubscription)))