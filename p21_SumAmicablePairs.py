#!/usr/bin/env python
import math

global all_sums
all_sums = {i: 0 for i in xrange(0,10001)}
count = 0

def d(n):
	ds = 1
	for i in xrange(2,int(math.ceil(math.sqrt(n)))):
		if (n % i == 0):
			ds += i + n/i
			if (i == math.ceil(math.sqrt(n))):
				ds -= i
	return ds

#generate sums of divisors for all numbers in [1,10000]
for n in xrange(1,10001):
	all_sums[n] = d(n)

for i in xrange(2,10001):
	if (all_sums[i] < 10001):
		if (all_sums[all_sums[i]] == i) and ( i != all_sums[i]):
			count += all_sums[i] + i
	
print count/2

