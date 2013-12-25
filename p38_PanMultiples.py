#!/usr/bin/env python
import utils
'''
all_nums = [i*(1..9) where i is the number currently examined]
returns the largest 9 pandigital number
formed from all_nums
return -1 if none can be found
'''
def check_prods(all_nums):
	# convert all the sums into strings for easy concatenation
	all_nums = [str(all_nums[i]) for i in xrange(0,len(all_nums))]
	tocheck = all_nums[0]
	checked = -1

	# keep concatenating each products to tocheck
	for i in xrange(1,len(all_nums)):
		tocheck += all_nums[i]
		#print "checking ", tocheck
		if len(str(tocheck)) > 9:
			break
		elif len(str(tocheck)) == 9 and utils.isPandigital(int(tocheck)):
			checked = int(tocheck)
			print "Tocheck",tocheck
	return checked

limit = 10000
results = []
for i in xrange(1000, limit):
	prods = [i]
	for n in xrange(2, 10):
		prods.append(i*n)
	k = check_prods(prods)
	if k != -1:
		results.append(k)

print results