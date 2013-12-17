#!/usr/bin/env python

def generate(n):
	fib1 = 1
	fib2 = 1
	cur = 1
	while cur < n:
		cur = fib1 + fib2
		if cur %2 == 0:
			yield cur
		yield 0
		fib1 = fib2
		fib2 = cur


print sum(generate(4000000))
