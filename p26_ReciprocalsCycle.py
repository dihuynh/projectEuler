
#!/usr/bin/env python
import math
import time


def reciprocalCycle(n):
	count = 1
	rem = 10 % n

	while rem != 1:
		rem = rem*10 % n
		count += 1
	return count


def main():
	limit = 1000
	maxLength = 0
	maxNum = 2
	x = 0

	for n in xrange(limit,2,-1):
		if (n % 2 != 0 and n % 5 != 0):
			x = reciprocalCycle(n)
			if ( x > maxLength):
				maxNum = n
				maxLength = x

	return maxNum

start = time.time()
print main()
print time.time() - start