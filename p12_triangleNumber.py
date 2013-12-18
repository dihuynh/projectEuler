#!/usr/bin/env python
import math

def generate_triangleNumber():
	numDivs = 2
	n = 1
	tri_num = 0
	while (numDivs <= 500):
		numDivs = 2
		tri_num = n*(n+1)/2
		for i in xrange(2,int(math.ceil(math.sqrt(tri_num)))):
			if (tri_num % i == 0):
				numDivs = numDivs + 2
		if (tri_num % int(math.sqrt(tri_num)) == 0):
			numDivs = numDivs -1

		n = n + 1

	return tri_num

print generate_triangleNumber()
