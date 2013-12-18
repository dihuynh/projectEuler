#!/usr/bin/env python
import sys

def get_list():
	nums = open("p13_number.txt")
	limit = 100
	index = 0
	allNums = []
	while (index < limit):
		num = nums.readline()
		allNums.append(int(num))
		print int(num), index
		index = index + 1

	return sum(allNums)

print get_list()