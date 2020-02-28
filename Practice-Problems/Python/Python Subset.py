for _ in range(int(input())):
    nA, Aelements, nB, Belements = int(input()), input().split(), int(input()), input().split()
    Aelements, Belements = set(Aelements), set(Belements)
    print(Aelements.issubset(Belements))