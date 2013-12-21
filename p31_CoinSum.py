#!/usr/bin/env python

# attempt at dynamic programming
# stole from http://www.mathblog.dk/project-euler-31-combinations-english-currency-denominations/ 
target = 200
coin_sizes = [1,2,5,10,20,50,100,200]
ways = [0] * (target+1)
ways[0]= 1

for i in xrange(0,len(coin_sizes)):
	# j is the amount of money
	for j in xrange(coin_sizes[i], target+1):
		# number of ways to make j amount is sum of 
		# the number of ways to make j-coin_size[i]
		# IOW: ways[100] = sum(ways[100-1], ways[100-2],...)
		ways[j] += ways[j-coin_sizes[i]]
		print ways[j]
	print
