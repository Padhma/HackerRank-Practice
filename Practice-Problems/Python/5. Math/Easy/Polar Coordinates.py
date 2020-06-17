import cmath as c

z = complex(input())

r, theta = c.polar(z)

print(r)
print(theta)

# Another Approach
# writing custom functions without using cmath

import math as m

def calculate_r(z):
	x = z.real
	y = z.imag
	return m.sqrt(x**2 + y**2)

def calculate_theta(z):
	x = z.real
	r = abs(z)
	return m.acos(x/r)

z = complex(input())
print(calculate_r(z))
print(calculate_theta(z))