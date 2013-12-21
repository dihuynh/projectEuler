#!/usr/bin/env python
# brute force, nothing too fancy
# generate a list of all primes up to 2 million (for no reasons)
# go through every possible combo of a and b and count the number 
# of consecutive primes

def primes (n):
	sieve = [True]*(n+1)
	for p in xrange(2,n+1):
			if sieve[p]:
				for i in xrange(p*p, n+1, p):
					sieve[i]=False
	return sieve

def f(n,a,b):
	return n**2+a*n+b

def main():
	sieve = primes(2000000)
	max_count = 0
	coeffs = [0,0]
	for a in xrange(-999,1000):
		for b in xrange(-999,1000):
			#print "Checking", a, b
			count = 0
			n = 0
			val = f(n,a,b)
			if (val>0):
				while sieve[f(n,a,b)]:
					count += 1
					n += 1
				if (count > max_count):
					coeffs[0] = a
					coeffs[1] = b
					max_count = count
	print coeffs[0]*coeffs[1], max_count

main()