#!/usr/bin/env python

#observation: a multiple of an abundant number is an abundant number
import math

global abundant
# a list of numbers we want, 
# aka numbers that can't be written as a sum of 2 abundant number
global valid 
limit = 28124
abundant = [False]*limit
valid = [True]*limit

def isPerfect(p):
	sum = 1
	for i in xrange(2,int(math.ceil(math.sqrt(p)))):
		if (p % i == 0):
			sum += i + p/i
			if (i == int(math.ceil(math.sqrt(p)))):
				sum -= i
	return sum == p

def isAbundant(p):
	sum = 1
	for i in xrange(2,int(math.ceil(math.sqrt(p)))):
		if (p % i == 0):
			sum += i + p/i
			if (i == int(math.ceil(math.sqrt(p)))):
				sum -= i
	return sum > p

def generate_abundant():
	abundant[12] = True
	for p in xrange(12,limit):
		if (not abundant[p]):
			abundant[p] = isAbundant(p)

		if (isPerfect(p)):
			for i in xrange(2*p, limit, p):
				abundant[i]=True

		if (abundant[p]):			
			for i in xrange(p*p, limit, p):
				abundant[i]=True

	#print [k for k in xrange(0,limit) if abundant[k]]

def get_sum():
	for i in xrange(0,limit):
		for j in xrange(0,limit):
			if (i+j<limit):
				if (abundant[i] and abundant[j] \
					  and valid[i+j]):
					valid[i+j] = False
			else:
				break
	return sum([k for k in xrange(0,limit) if valid[k]])


generate_abundant()
print get_sum()
