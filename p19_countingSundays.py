#!/usr/bin/env python

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

total_days = 0
count = 0
for i in xrange(1901,2001):
	for month in days_in_month:
		total_days += month
		if (month == 28 and i % 4 == 0):
			total_days += 1
		if (total_days % 7 == 5):
			count += 1
print count