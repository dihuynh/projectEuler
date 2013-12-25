#!/usr/bin/env python

# a sieve to generate primes up to limit, inclusive
def get_primes (n):
	sieve = [True]*(n+1)
	sieve[0] = False
	sieve[1] = False
	for p in xrange(2,n+1):
			if sieve[p]:
				for i in xrange(p*p, n+1, p):
					sieve[i]=False
	return sieve


# for pandigital problems
def no_repeat_digit(a):
	return len(set(list(str(a)))) == len(list(str(a)))

def no_common_digit(m,n): 
	sm = set(list(str(m)))
	sn = set(list(str(n)))
	return len(sm.intersection(sn)) == 0

def no_zeros(n):
	 return '0' not in list(str(n))

# for cleaner code
def isPandigital(n):
	# parse n into a list of digits
	all_digits = [int(x) for x in list(str(n))]
	for i in xrange(1,len(all_digits)+1):
		if i not in all_digits:
			return False
	return no_repeat_digit(n)


	all_primes = utils.get_primes(7654321)

