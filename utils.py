#!/usr/bin/env python

# a sieve to generate primes up to limit, inclusive
def get_primes (n):
	sieve = [True]*(n+1)
	for p in xrange(2,n+1):
			if sieve[p]:
				for i in xrange(p*p, n+1, p):
					sieve[i]=False
	return sieve