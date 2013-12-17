#!/usr/bin/env python

def primes (n):
	ps = []
	sieve = [True]*(n+1)

	for p in xrange(2,n+1):
			if sieve[p]:
				ps.append(p)
				for i in xrange(p*p, n+1, p):
					sieve[i]=False
	return ps[10000]

print primes(1000000)


