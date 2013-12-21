#!/usr/bin/env python

limit = 9**5*6 + 1 
total =0
for i in xrange(6,limit):
	digits =  list(str(i))
	sum_digits = 0
	# print "Checking", i
	for d in digits:
		print d,
		sum_digits += int(d)**5
	if (i == sum_digits):
		total += sum_digits

print total
