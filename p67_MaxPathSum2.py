#!/usr/bin/env python

def strip_newlines(lists):
	new_lists = []
	for i in lists:
		new_lists.append(i.rstrip())

	another_one = []
	for k in new_lists:
		another_one.append([int(j) for j in k.split()])
	return another_one

# replace an element with the sum of it and the bigger number 
# on top of it
#  2            2           15
# 3 4 -------> 8 13 ----->  
#3 5 9
def get_max_path(lists):
	for i in xrange(len(lists)-2,-1,-1):
		for j in xrange(0,i+1):
			lists[i][j] += max([lists[i+1][j], lists[i+1][j+1]])
	return lists[0][0]

triangle = open("p67_triangle.txt").readlines()
# triangle = open("small_test.txt").readlines()
lists = strip_newlines(triangle)
print get_max_path(lists)