#!/usr/bin/env python


def digital_sum(a,b):
	n = a**b
	total = []
	for i in list(str(n)):
		total.append(int(i))
	return sum(total)


def main():
	maximum = 0
	for a in xrange(2,101):
		for b in xrange(2,101):
			maximum = max(digital_sum(a,b), maximum)
	print maximum

main()