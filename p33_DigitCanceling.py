#!/usr/bin/env python
import operator as op

valid = []

def truncatable(ab,cd):
	b = ab % 10
	a = (ab - b)/10
	d = cd % 10
	c = (cd - d)/10
	if (b == c): 
	 return (10*a*d + b*d == 10*a*b + a*d)
	elif (a == d):
		return (10*a*c + b*c == 10*c*b + a*b)
	else:
		return False 

# multiply and reduce every tuples in the tuples list
def multiply_all (tuples):

	nums = []
	denoms = []
	for i in xrange(0,len(tuples)):
		nums.append(tuples[i][0])
		denoms.append(tuples[i][1])

	num = reduce(op.mul,nums,1)
	denom = reduce(op.mul,denoms,1)

	return denom/gcd(num,denom)

# Euclidean algorithm
def gcd (a,b):
	while (a != b):
		if a > b:
			a = a - b
		else:
			b = b - a
	return a


def main():
	for i in xrange (10,100):
		for j in xrange(i+1,100):
			if ( i % 10 != 0 and j % 10 != 0 and i < j):
				if truncatable(i,j):
					valid.append((i,j))
	return multiply_all(valid)


print main()
