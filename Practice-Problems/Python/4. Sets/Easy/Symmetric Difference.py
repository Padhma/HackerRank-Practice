m, a, n, b = int(input()), input().split(), int(input()), input().split()

[print(i) for i in sorted(set(a)^set(b), key=int)]