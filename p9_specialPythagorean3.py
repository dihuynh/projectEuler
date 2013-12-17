#!/usr/bin/env python


def get_result():
	for i in xrange(1,1000):
		for j in xrange(1,1000):
			k = 1000 - j - i
			c = max(i,j,k)
			a = min(i,j,k)
			b = (i+j+k) - c - a
			if (c*c == a*a + b*b):
				return a*c*b

print get_result()