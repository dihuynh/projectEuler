#!/usr/bin/env python

def get_primes_list (n):
	ps = []
	sieve = [True]*(n+1)

	for p in xrange(2,n+1):
			if sieve[p]:
				ps.append(p)
				for i in xrange(p*p, n+1, p):
					sieve[i]=False
	return ps

def sum_primes(n):
	allPrimes = get_primes_list(n)
	return sum(allPrimes)


print sum_primes(2000000)