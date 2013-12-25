#!/usr/bin/env python
import itertools
import time

digits = [0,1,2,3,4,5,6,7,8,9]
valid = set()

def no_repeat_digit(a):
	return len(set(list(str(a)))) == len(list(str(a)))

def no_common_digit(m,n): 
	sm = set(list(str(m)))
	sn = set(list(str(n)))
	return len(sm.intersection(sn)) == 0

def no_zeros(n):
	 return '0' not in list(str(n))

# for cleaner code
def valid(n):
	return no_zeros(n) and no_repeat_digit(n)

products = []
# 1 of 2 cases: 2 digits * 3 digits
for a in xrange(10,99):
	if valid(a):
		for b in xrange(100,999):
			if no_common_digit(a,b) and valid(b):
				c = a * b
				if len(str(c)) == 4 and valid(c)\
					and no_common_digit(a,c) and no_common_digit(b,c):
					products.append(c)

# 2 of 2 cases: 1 digits * 4 digits
for a in xrange(1,9):
	for b in xrange(1000,9999):
		if no_common_digit(a,b) and valid(b):
				c = a * b
				if len(str(c)) == 4 and valid(c)\
					and no_common_digit(a,c) and no_common_digit(b,c):
					products.append(c)

print sum(set(products))