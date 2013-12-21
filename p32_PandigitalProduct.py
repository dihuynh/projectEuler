#!/usr/bin/env python
import itertools

digits = [0,1,2,3,4,5,6,7,8,9]
valid = set()

def toInt(l):
	n = ""
	for i in l:
		n += str(i)
	return int(n)

def get_first23():
	first =[]
	for i in xrange(1,len(digits)):
		first.append(i)
		for j in xrange(1,len(digits)):
			if (i != j):
				first.append(j)
				num1 = toInt(first)
				yield num1
				first.remove(j)
		first.remove(i)

def get_left(l):
	return itertools.permutations([x for x in digits if x not in l and x != 0])

def get_first14():
	first =[]
	for i in xrange(1,len(digits)):
		first.append(i)
		print 
		for j in xrange(1,len(digits)):
			if (i != j):
				first.append(j)
				num1 = toInt(first)
				yield num1
				first.remove(j)
		first.remove(i)

def get_all23():
	for f in get_all23():
		print f,
		for s in getleft(f):
			print s,
		print 