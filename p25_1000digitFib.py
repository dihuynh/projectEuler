#!/usr/bin/env python

import math

def fib():
	fib1 = 1
	fib2 = 1
	cur = 1
	count = 2
	while len(str(cur)) < 1000:
		cur = fib1 + fib2
		fib1 = fib2
		fib2 = cur
		count += 1
	print count

fib()