#!/usr/bin/env python

import utils

def prime_sums(sieve):
	sums = [0]*len(sieve)
	for i in xrange(0,len(sieve)):
		if sieve[i]:
			sums[i] += i
		else:
			sums[i] = -1
	print sums






# generate enough primes
sieve = utils.get_primes(10*6)
sums = prime_sums(sieve)
# to store the sum and length in format:
# [sum] = length of sum (number of primes that adds to sum)	
results = dict()

primes = [x for x in xrange(0,len(sieve)) if sieve[x]]

for i in xrange(0, len(sums)):
	if sieve[sums[i]]:
		results[sums[i]] = primes.index(i) # get the position of i in primes
	else:
prime_sums(sieve)