#!/usr/bin/env python
import math as m

def nchoosek (n,k):
	return m.factorial(n)/(m.factorial(k)*m.factorial(n-k))

# returns the number of digits in this number
def numDigits (n):
	return len(str(n))


def main():
	count = 0
	for n in xrange(1,101):
		for k in xrange(1,n):
			if (numDigits(nchoosek(n,k)) >= 7):
				print nchoosek(n,k)
				count += 1
	return count

print main()
