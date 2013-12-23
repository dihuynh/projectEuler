#!/usr/bin/env python
import math


# a number is triangle if it's in this form:
# 1/2*(2k - 1/2)^2 - 1/8 = n 
def isHexagonal (n):
	rem = n + .125
	return isInt(.5*(math.sqrt(2*rem)+.5))


def isInt (n):
	return math.ceil(n) == math.floor(n)

# a number is triangle if it's in this form:
# 1/2*(k + 1/2)^2 - 1/8 = n 
def isTriangle (n):
	rem = n + .125
	return isInt(math.sqrt(2*rem)-.5)

def generate_pent(n):
	return n*(3*n-1)/2  

def main():
	found = False
	i = 2
	while not found:
		p = generate_pent(i)
		if isTriangle(p) and isHexagonal(p):
			print p
		i += 1


print main()



