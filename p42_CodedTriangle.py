#!/usr/bin/env python
import re
import math

def get_score(word):
	score = 0
	for i in list(word):
		score += ord(i)- 64
	return score

def isInt (n):
	return math.ceil(n) == math.floor(n)

def isTriangle (n):
	rem = n + .125
	return isInt(math.sqrt(2*rem)-.5)

def main():	
	names = open("p42_words.txt").readline()
	all_names = re.split('","|"',names)[1:-1]
	count = 0

	for i in all_names:
		if isTriangle(get_score(i)):
			count += 1
	print count

main()