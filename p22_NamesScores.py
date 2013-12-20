#!/usr/bin/env python
import re

global score
score = dict()
names = open("p22_names.txt").readline()
all_names = re.split('","|"',names)[:-1]
all_names.sort()
total = 0

def get_score(word):
	score = 0
	for i in list(word):
		score += ord(i)- 64
	return score

for index in xrange(0,len(all_names)):
	score = get_score(all_names[index])
	total += (index) * score

print total