#!/usr/bin/env python
import math

all_powers = set()

for i in xrange(2,101):
	for j in xrange(2,101):
		all_powers.add(math.pow(i,j))

print len(all_powers)