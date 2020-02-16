def evalpoly(p, x):
    return sum( [ eval(p.replace('x', str(x))) ] )

x, k = input().split()

polynomial = input()

polySum = evalpoly(polynomial, x)

if(polySum == int(k)):
    print(True)
else:
    print(False)