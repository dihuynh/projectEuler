#!/usr/bin/env python
import sys
import math

def primes (k):
		n = int(math.ceil(math.sqrt(k)))
		ps = []
		sieve = [True]*(n+1)
		for p in xrange(2,n+1):
				if sieve[p]:
					if k % p == 0:
						ps.append(p)
					for i in xrange(p*p, n+1, p):
						sieve[i]=False
		return ps


print primes(int(sys.argv[1]))[-1]