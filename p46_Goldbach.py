#!/usr/bin/env python
import math

def primes (n):
	sieve = [True]*(n+1)
	for p in xrange(2,n+1):
			if sieve[p]:
				for i in xrange(p*p, n+1, p):
					sieve[i]=False
	return sieve


def goldbach(n,sieve):
	for i in xrange(1,int(math.ceil(math.sqrt(n)))):
		remainder = n - i**2*2
		# if the remainder is prime
		if (remainder>0):
			if sieve[remainder]:
				return True
	return False

def main():
	sieve = primes(100000)
	for i in xrange(9,len(sieve)):
		if (not sieve[i] and i%2 == 1):
			if not goldbach(i,sieve):
				return i
	return -1

print main()