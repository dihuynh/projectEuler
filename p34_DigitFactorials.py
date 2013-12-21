#!/usr/bin/env python
import math

#values of the factorials from 0 - 9
factorials = [1,1,2,6,24,120,720,5040,40320,362880]
# because 9!*8 also has 7 digits
limit = factorials[9]*7


total = 0
for i in xrange(7,limit+1):
	fact_digits = sum([factorials[int(x)] for x in list(str(i))]) 
	if i == fact_digits:
		total += i

print total