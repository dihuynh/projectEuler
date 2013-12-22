#!/usr/bin/env python


# upper bound after some math
# number of digits up to 99999
# 9 numbers with 1 digit, 90 with 2 digits...
under_mil = 9+90*2+900*3+9000*4+90000*5
#the number of numbers we need in the 6 digits range 
six_digits = (10**6 - under_mil)/6 + 10**5

d = ""
for i in xrange(0, six_digits+1):
	d += str(i)

product = 1
for j in xrange(0,7):
	product *= int(d[10**j])

print product