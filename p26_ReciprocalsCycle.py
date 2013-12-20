#!/usr/bin/env python
import math

def isInt(n):
	return math.ceil(n) == math.floor(n)

def get_cycles_length(n):
	#keep a list of recurring digits
	#the length of this list is the reciprocal cycle length
	cycle = []
	over = 10
	print "what", over%n 

	while (over % n != 1):
		div = over/n
		remainder = over % n
		cycle.append(div)
		over = remainder*10

	return len(cycle)

max_cycle = 0
for i in xrange(1000,2,-1):
	cycle = get_cycles_length(i)
	print "Cycle", cycle
	max_cycle = max(cycle,max_cycle)

print max_cycle