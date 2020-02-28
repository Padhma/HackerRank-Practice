nE, english, nF, french = int(input()), input().split(), int(input()), input().split()

englishSet, frenchSet = set(english), set(french)

diff = englishSet.difference(frenchSet)

print(len(diff))