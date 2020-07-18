import numpy as np
coefficients_P = list(map(float, input().split()))
x = int(input())
print(np.polyval(coefficients_P,x))