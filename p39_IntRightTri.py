#!/usr/bin/env python
import operator

global triples
global counts

triples = dict()
counts = dict()
counts = [0]*1001


for c in xrange(1, 1001):
	for b in xrange(1, c):
		for a in xrange(1,b):
			if c**2 == a**2 + b**2 and (a+b+c)<=1000:
				counts[a+b+c] += 1
				print a+b+c, counts[a+b+c]

max_val = 0
max_key = 0

for i in xrange(0,len(counts)):
	if (max_val < counts[i]):
		max_val = counts[i]
		max_key = i


print max_key, max_val