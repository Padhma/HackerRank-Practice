
from itertools import product

a, b = [map(int, input().split()) for _ in range(2)]

print(*product(a, b))
