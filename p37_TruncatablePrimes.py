#!/usr/bin/env python

def primes (n):
	sieve = [True]*(n+1)
	sieve[0] = False
	sieve[1] = False
	for p in xrange(2,n+1):
			if sieve[p]:
				for i in xrange(p*p, n+1, p):
					sieve[i]=False
	return sieve

# we kn	ow that n is prime
def truncatable(n,sieve):
	temp1 = n
	#left to right abcd, bcd, cd, d
	while (sieve[temp1] and temp1 != 0):
		i = temp1%10**(len(str(temp1))-1)
		temp1 = i
	
	#right to left abcd, abc, ab, a
	temp2 = n
	while (sieve[temp2] and temp2 != 0):
		i = temp2/10
		temp2 = i
	if temp2 == 0 and temp1 == 0:
		return True
	else:
		return False

def main():
	limit = 2000000
	sieve =	primes(limit)
	valid = []
	for i in xrange(11,limit):
		print i
		if sieve[i] and len(valid) != 11 :
			if truncatable(i,sieve):
				valid.append(i)
	return sum(valid)


print main()