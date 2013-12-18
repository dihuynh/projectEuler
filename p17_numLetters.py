#!/usr/bin/env python

# number of letters for 1-9
ones = ["", "one", "two","three",\
		"four", "five","six",\
		"seven", "eight", "nine"]

# number of letters for 10,20,...100
tens = ["","ten", "twenty", "thirty",\
		"forty", "fifty", "sixty",\
		"seventy", "eighty", "ninety"]

# number of letters for 11-19
teens = ["","eleven", "twelve", "thirteen",\
		 "fourteen", "fifteen", "sixteen",\
		 "seventeen", "eighteen","nineteen"]

hundreds = ["","onehundred", "twohundred", "threehundred",\
			"fourhundred", "fivehundred", "sixhundred",\
			"sevenhundred", "eighthundred", "ninehundred",\
			"onethousand"]
total =0

for i in xrange(0,1001):
#	print "Number: ", i,
	
	#print "	Adding ones", i%10
	count = hundreds[i/100]
	#print "	Adding the hundreds place", i/100
	if (i/100 > 0 and i%100 != 0):
		count += "and"
		#print "	Adding and"

	if (i>=100):
		i = i%100
		if (i/10 == 1 and i%10 != 0):
			count += teens[i%10]
			#print "	Adding teens"
		else:
			#print "	Adding tens"
			count += ones[i%10]
			count += tens[i/10]
	else:
		if (i/10 == 1 and i%10 != 0):
			count += teens[i%10]
			#print "	Adding teens"
		else:
			#print "	Adding tens"
			count += ones[i%10]
			count += tens[i/10]
	
	total += len(count)
#	print "	Count: ", count, + len(count)

print "Total", total