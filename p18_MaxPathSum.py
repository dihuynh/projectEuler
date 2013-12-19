#!/usr/bin/env python

def strip_newlines(lists):
	new_lists = []
	for i in lists:
		new_lists.append(i.rstrip())

	another_one = []
	for k in new_lists:
		another_one.append([int(j) for j in k.split()])
	return another_one

def get_max_path(lists):
	last_line = lists[-1]
	#print lists
	max_path = 0
	for i in xrange(0,len(last_line)):
		up = len(last_line)-2
		cur_path = last_line[i]
		print "\nGetting max path from", cur_path
		right = i
		
		while (up >= 0):
			if (right == 0):
				cur_path += lists[up][0]
				# print "0 case",lists[up][0]
				right = 0
			elif (right == len(lists[up])-1):
				cur_path += lists[up][len(lists[up])-1]
				# print "last case",lists[up][len(lists[up])-1]
				right = len(lists[up])-2
			else:
				if (lists[up][right] > lists[up][right-1]):
					cur_path += lists[up][right]
					# print "right case",lists[up][right]
				else:
					cur_path += lists[up][right-1]
					# print "left case",lists[up][right+1]
					right -=1
			up -= 1	
		#print "\nTotal current path is", cur_path
		max_path = max(max_path,cur_path)

	return max_path

triangle = open("p18_triangle.txt").readlines()
lists = strip_newlines(triangle)
print get_max_path(lists)