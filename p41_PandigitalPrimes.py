#!/usr/bin/env python

import utils
import time

# brute force is way too slow
# consider digit sum:
#
# 1+2+3+4+5+6+7+8+9 = 45
# 1+2+3+4+5+6+7+8 = 36
# 1+2+3+4+5+6+7 = 28
# 1+2+3+4+5+6 = 21
# 1+2+3+4+5 = 15
# 1+2+3+4 = 10
# 1+2+3 = 6
# 1+2 = 3
#
# everything but 4 and 7 is divisible by 3 so we
# only need to check those two. 

s = time.time()
all_primes = utils.get_primes(7654321)
answer = []

for i in xrange(0,len(all_primes)):
	if (len(str(i)) == 4 or len(str(i))==7):
		if all_primes[i]:
			if utils.isPandigital(i):
				answer.append(i)

print answer[-1]
print time.time() - s